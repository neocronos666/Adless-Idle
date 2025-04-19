# engine/utils/logger.py

import logging
import os
from datetime import datetime

def setup_logger(name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    today = datetime.now().strftime("%y%m%d")
    log_path = os.path.join(log_dir, f"{today}_{name.upper()}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')
        formatter = logging.Formatter("\n⚙️  === LOG ENTRY ===\n%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

