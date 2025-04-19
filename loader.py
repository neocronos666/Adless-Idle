# loader.py

import os
import json
from pathlib import Path
from datetime import datetime
from logger import log_missing
# ------------------------------------
# 👤 CONFIURACION POR DEFECTO
# ------------------------------------
SETTINGS_PATH = Path("settings.json")
USERS_DIR = Path("users")
CAMPAIGNS_DIR = Path("campaigns")
LOG_FILE = Path("logs/loader.log")
DEFAULT_USER = "default.json"
# Plantilla base para settings de prueba (borrar y se crea de aquí)
DEFAULT_SETTINGS = {
    "debug": True,
    "current_user": "default"
}
# Plantilla base para usuario (borrar y se crea de aquí)
DEFAULT_USER_DATA = {
    "language": "es",
    "theme": "dark",
    "screen": {
        "width": 1024,
        "height": 768,
        "fullscreen": False
    },
    "progress": {}
}

# ------------------------------------
# 🔧 Configurador de settings
# ------------------------------------

def set_settings(settings: dict = DEFAULT_SETTINGS) -> None:
    """Escribe el archivo de settings con los valores pasados."""
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

# ------------------------------------
# 🔄 Cargador de settings
# ------------------------------------

def load_settings() -> dict:
    """Carga el archivo settings.json. Si no existe, lo crea con la plantilla y verifica integridad mínima."""
    if not SETTINGS_PATH.exists():
        set_settings(DEFAULT_SETTINGS)

    with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
        settings = json.load(f)
    if not isinstance(settings, dict) or not settings:
        raise ValueError("El archivo settings.json está vacío o mal formado.")
    return settings

# ------------------------------------
# 👤 Configuración de usuario
# ------------------------------------
def set_user(user_name: str = "default", user_data: dict = None) -> None:
    """Crea el archivo de usuario con configuración por defecto o personalizada."""
    USERS_DIR.mkdir(exist_ok=True)
    if user_data is None:
        user_data = DEFAULT_USER_DATA
    user_path = USERS_DIR / f"{user_name}.json"
    with open(user_path, "w", encoding="utf-8") as f:
        json.dump(user_data, f, indent=4)

def load_user(user_name: str = None) -> dict:
    """Carga el archivo del usuario actual, o crea uno default si no existe."""
    settings = load_settings()
    user_name = user_name or settings.get("current_user", "default")
    user_path = USERS_DIR / f"{user_name}.json"

    if not user_path.exists():
        set_user(user_name)

    with open(user_path, "r", encoding="utf-8") as f:
        user_data = json.load(f)

    return user_data
# ------------------------------------
# 🔄 Cargador de Campaña
# ------------------------------------

def check_campaign_paths(campaign_name: str) -> list[str]:
    base_path = os.path.join("campaigns", campaign_name)
    missing = []

    # Config principal de la campaña
    config_path = os.path.join(base_path, "config.json")
    if not os.path.exists(config_path):
        missing.append(config_path)

    # Imagen de fondo
    bg_found = any(os.path.exists(os.path.join(base_path, "images", f"bg.{ext}")) for ext in ["jpg", "png", "svg"])
    if not bg_found:
        missing.append("background image")

    # Textos intro y outro
    for tfile in ["intro.json", "outro.json"]:
        if not os.path.exists(os.path.join(base_path, "texts", tfile)):
            missing.append(f"texts/{tfile}")

    # Entidades: al menos una válida (desde track001.json hasta track999.json)
    track_found = False
    for i in range(1, 1000):
        track_id = f"track{i:03d}.json"
        track_path = os.path.join(base_path, "entities", track_id)
        if os.path.exists(track_path):
            track_found = True
            break

    if not track_found:
        missing.append("at least one track (track001.json+)")

    return missing


def load_campaign(campaign_name: str) -> dict:
    base_path = os.path.join("campaigns", campaign_name)
    result = {
        "config": None,
        "estado": "fallida"
    }

    if not os.path.exists(base_path):
        if settings.get("debug"):
            log_missing([f"Carpeta de campaña no encontrada: {base_path}"], source="LOADER")
        return result

    config_path = os.path.join(base_path, "config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                result["config"] = json.load(f)
        except Exception as e:
            if settings.get("debug"):
                log_missing([f"Error al cargar config.json: {str(e)}"], source="LOADER")
            return result

    missing = check_campaign_paths(campaign_name)

    if not missing:
        result["estado"] = "completa"
    elif os.path.exists(config_path):
        result["estado"] = "incompleta"
    else:
        result["estado"] = "fallida"

    log_missing(missing, source="LOADER")
    return result
