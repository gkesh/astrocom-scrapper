from os import path
from typing import Callable

import logging


STATIC = f"{path.dirname(path.abspath(__file__))}/static"
LOG_FILE = f"{STATIC}/astrocom.log"

DATE_FORMAT =  "%d-%b-%y %H:%M:%S"
LOG_FORMAT = "[%(asctime)s]%(message)s"

logger = logging.getLogger("comigration")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(LOG_FILE)

formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARN)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

levels = {
    logging.INFO: logger.info,
    logging.WARN: logger.warn,
    logging.DEBUG: logger.debug,
    logging.ERROR: logger.error
}

def loggers(level: int) -> Callable:
    def typelog(message_maker: Callable) -> Callable:
        def inner(*args, **kwargs):
            message = message_maker(*args, **kwargs)
            levels[level](message)
        return inner
    return typelog
