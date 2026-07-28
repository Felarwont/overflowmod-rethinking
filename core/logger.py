import logging

def setup_logger() -> None:
    logger = logging.getLogger("overflowmod")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s -- %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)