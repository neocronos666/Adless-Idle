# engine/utils/default_theme.py

DEFAULT_THEME_JSON = {
    "name": "Default",
    "description": "Tema retro cyberpunk para Adless Idle",
    "version": "1.0",
    "engine_version": ">=1.0.0",
    "mode": "dark",
    "fonts": {
        "main": "Poppins",
        "secondary": "Quicksand",
        "typed_text": "IM_Fell_DW_Pica_SC"
    },
    "fallback_fonts": True,
    "layout": "adaptive",
    "hud": {
        "blocks": ["menu", "score", "tracks", "info", "progress_bar"],
        "hidden": []
    },
    "sounds": {
        "click": "click.wav",
        "notification": "notif.ogg"
    },
    "background": {
        "light": "backgrounds/light.svg",
        "dark": "backgrounds/dark.svg"
    }
}

DEFAULT_HUD_CONFIG = {
    "screen_ratio": "9:16",
    "layout": {
        "menu_position": "top-left",
        "score_position": "top-right",
        "tracks_position": "left",
        "info_position": "right",
        "progress_bar_position": "bottom"
    },
    "margins": {
        "top": 10,
        "left": 10,
        "right": 10,
        "bottom": 10
    },
    "block_size": {
        "menu": [80, 40],
        "track_button": [120, 60],
        "info": [320, 640],
        "progress_bar": [400, 20]
    }
}

DEFAULT_PALETTE_CSS = """
/* === Light Mode === */
:root {
  --color-1-light: #42b846;
  --color-2-light: #9e22b4;
  --color-3-light: #ffffff;
  --color-4-light: #000000;
  --color-5-light: #eb1e62;
}

/* === Dark Mode === */
:root {
  --color-1-dark: #1f6a2b;
  --color-2-dark: #5a0e6e;
  --color-3-dark: #eeeeee;
  --color-4-dark: #111111;
  --color-5-dark: #b8133f;
}
"""

