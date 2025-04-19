import os
import json
from datetime import datetime
from packaging import version
from packaging.specifiers import SpecifierSet
from engine.utils.css_parser import parse_palette_css
from engine.utils.logger import setup_logger
from engine.utils.default_theme import DEFAULT_THEME_JSON, DEFAULT_HUD_CONFIG, DEFAULT_PALETTE_CSS

class ThemeLoader:
    def __init__(self, theme_name="default", engine_version="1.0.0", debug=False):
        self.theme_name = theme_name
        self.engine_version = engine_version
        self.debug = debug

        self.theme_dir = os.path.join("themes", self.theme_name)
        self.logger = setup_logger("THEME") if self.debug else None

        self.theme_json_path = os.path.join(self.theme_dir, "theme.json")
        self.hud_config_path = os.path.join(self.theme_dir, "hud_config.json")
        self.palette_path = os.path.join(self.theme_dir, "palette.css")

        self.theme_data = {}
        self.ensure_files_exist()
        self.load_theme()

    def log(self, msg):
        if self.logger:
            self.logger.info(msg)

    def ensure_files_exist(self):
        os.makedirs(self.theme_dir, exist_ok=True)
        os.makedirs(os.path.join(self.theme_dir, "fonts"), exist_ok=True)
        os.makedirs(os.path.join(self.theme_dir, "sounds"), exist_ok=True)
        os.makedirs(os.path.join(self.theme_dir, "backgrounds"), exist_ok=True)

        if not os.path.exists(self.theme_json_path):
            with open(self.theme_json_path, "w") as f:
                json.dump(DEFAULT_THEME_JSON, f, indent=2)
            self.log("Creado theme.json por defecto")

        if not os.path.exists(self.hud_config_path):
            with open(self.hud_config_path, "w") as f:
                json.dump(DEFAULT_HUD_CONFIG, f, indent=2)
            self.log("Creado hud_config.json por defecto")

        if not os.path.exists(self.palette_path):
            with open(self.palette_path, "w") as f:
                f.write(DEFAULT_PALETTE_CSS)
            self.log("Creado palette.css por defecto")

    def validate_engine_version(self, required_version):
        #if not version.parse(self.engine_version) in version.SpecifierSet(required_version):
        if not version.parse(self.engine_version) in SpecifierSet(required_version):

            raise ValueError(f"El tema requiere engine_version {required_version}, pero se está usando {self.engine_version}.")

    def load_theme(self):
        with open(self.theme_json_path, "r") as f:
            theme_json = json.load(f)

        self.validate_engine_version(theme_json.get("engine_version", ">=1.0.0"))

        mode = theme_json.get("mode", "dark")
        palette = parse_palette_css(self.palette_path, mode)

        fonts = theme_json.get("fonts", {})
        fonts_paths = {}
        for k, font_name in fonts.items():
            local_path = os.path.join(self.theme_dir, "fonts", f"{font_name}.ttf")
            fonts_paths[k] = local_path if os.path.exists(local_path) else font_name

        with open(self.hud_config_path, "r") as f:
            hud_config = json.load(f)

        self.theme_data = {
            "name": theme_json.get("name", self.theme_name),
            "version": theme_json.get("version", "1.0"),
            "mode": mode,
            "palette": palette,
            "fonts": {
                **fonts,
                "paths": fonts_paths
            },
            "hud": {
                "layout": hud_config.get("layout", {}),
                "hidden_blocks": theme_json.get("hud", {}).get("hidden", []),
                "block_size": hud_config.get("block_size", {})
            },
            "sounds": theme_json.get("sounds", {}),
            "background": theme_json.get("background", {}).get(mode, None)
        }

        self.log(f"Tema '{self.theme_name}' cargado correctamente")

    def get_theme_data(self):
        return self.theme_data

