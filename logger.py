import os
import logging
from datetime import datetime
import json

# Ruta y nombre del archivo settings
SETTINGS_FILE = "settings.json"

# Función para verificar si el modo debug está activado
def is_debug_mode():
    if not os.path.exists(SETTINGS_FILE):
        return False
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
            return settings.get("debug", False)
    except Exception:
        return False

# Función para inicializar un logger
def setup_logger(source_name: str):
    if not is_debug_mode():
        return None  # Logging desactivado si no está en modo debug

    # Crear carpeta de logs si no existe
    os.makedirs("logs", exist_ok=True)

    # Obtener fecha actual y construir nombre del archivo
    date_str = datetime.now().strftime("%y%m%d")
    log_filename = f"logs/{date_str}_{source_name.upper()}.log"

    # Crear logger
    logger = logging.getLogger(source_name)
    logger.setLevel(logging.DEBUG)

    # Verificar si ya tiene handler (para no duplicar logs)
    if not logger.handlers:
        file_handler = logging.FileHandler(log_filename, encoding='utf-8')
        formatter = logging.Formatter(
            "\n════════════════════════════════════════════════\n"
            "[%(asctime)s] - %(message)s\n"
            "════════════════════════════════════════════════",
            "%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def log_missing(missing_files: list[str], source: str = "LOADER") -> None:
    # Verifica si el modo debug está activo
    from loader import settings  # Asegurate que `settings` esté cargado en loader.py antes
    if not settings.get("debug", False):
        return

    if not missing_files:
        return

    now = datetime.now()
    date_str = now.strftime("%y%m%d")
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{date_str}_{source.upper()}.log")

    separator = "─" * 60
    log_entry = f'''
        {separator}
        ⏱️ {time_str}
        🚨 Archivos faltantes detectados:
        ''' + "\n".join(f"- {f}" for f in missing_files) + f"\n{separator}\n"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

