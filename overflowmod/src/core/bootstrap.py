import logging

def setup_logger() -> None:
    logger = logging.getLogger("overflowmod")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s -- %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

def load_handlers() -> None:
    from overflowmod.src.players import handlers
    from overflowmod.src.core.polling import pollings

def apply_patches() -> None:
    from overflowmod.src import patches

    patches.apply_session_patches()
    patches.apply_game_activity_patches()