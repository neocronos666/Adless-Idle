# loader.py

import os
import json
from pathlib import Path
from datetime import datetime

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

def log_missing(path: Path):
    pass

def load_campaign(campaign_name: str) -> dict:
    pass

def check_required_campaign_files(campaign_dir: Path) -> list:
    pass
