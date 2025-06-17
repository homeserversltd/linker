import logging
import os
from config import LOG_PATH

def get_logger(name="linker"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
    return logger
