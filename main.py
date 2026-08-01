# ba_meta require api 9
import logging

import babase

from overflowmod.src.core import bootstrap

def main():
    bootstrap.setup_logger()
    bootstrap.load_handlers()
    bootstrap.apply_patches()

# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        main()

        from app import polling
        polling.start()

        logger = logging.getLogger("overflowmod")
        logger.info("overflowmod started!")

        return super().on_app_running()

    def on_app_shutdown_complete(self):
        from app import db

        db.close()

        logger = logging.getLogger("overflowmod")
        logger.debug("Database closed")
        return super().on_app_shutdown_complete()