from logger import loggers
import logging


@loggers(logging.INFO)
def info(module: str, message: str) -> None:
    return f"[INFO][{module}] - {message}"


@loggers(logging.ERROR)
def error(module: str, message: str) -> None:
    return f"[ERROR][{module}] - {message}"


@loggers(logging.WARN)
def warn(module: str, message: str) -> None:
    return f"[WARNING][{module}] - {message}"


@loggers(logging.DEBUG)
def debug(module: str, message: str) -> None:
    return f"[DEBUG][{module}] - {message}"