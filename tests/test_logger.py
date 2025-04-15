# Asegura que la raíz del proyecto esté en el path
import sys
import os
import json
import glob


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime

from logger import setup_logger

def test_logger_creates_file_and_logs_messages():
    # Paso 1: Crear un archivo de configuración temporal con debug activado
    settings = {
        "debug": True
    }
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f)

    # Paso 2: Configurar logger
    logger = setup_logger("TEST")

    assert logger is not None

    # Paso 3: Escribir varios tipos de mensajes
    logger.debug("Mensaje DEBUG de prueba")
    logger.info("Mensaje INFO de prueba")
    logger.warning("Mensaje WARNING de prueba")
    logger.error("Mensaje ERROR de prueba")
    logger.critical("Mensaje CRITICAL de prueba")

    # Paso 4: Verificar que el archivo de log fue creado
    date_str = datetime.now().strftime("%y%m%d")
    expected_filename_pattern = f"logs/{date_str}_TEST.log"

    matching_files = glob.glob(expected_filename_pattern)
    assert matching_files, "No se encontró el archivo de log"

    # Paso 5: Leer el archivo y verificar que contiene al menos un mensaje
    with open(matching_files[0], "r", encoding="utf-8") as f:
        content = f.read()
        assert "Mensaje DEBUG de prueba" in content
        assert "Mensaje INFO de prueba" in content
        assert "Mensaje WARNING de prueba" in content
        assert "Mensaje ERROR de prueba" in content
        assert "Mensaje CRITICAL de prueba" in content

