import logging

from src.config import configurator


logger = logging.getLogger("backup")
handler = logging.FileHandler(filename=configurator.logs_file, mode="a", encoding="utf-8")
formatter = logging.Formatter(fmt="{asctime} {levelname} {message}", style="{", datefmt=configurator.time_format)

logger.addHandler(handler)
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
