import logging
import sys


def get_logger(
        name: str,  # todo: check if name is needed
        level: int = logging.INFO,
        fmt: str = "%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s"
        # todo: check what is the default format
) -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)

    return logger
