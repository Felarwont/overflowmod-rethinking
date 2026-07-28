# ba_meta require api 9
import logging

import babase

from core.logger import setup_logger

def load_handlers():
    from player import handlers
    from core.polling import pollings

def main():
    load_handlers()

setup_logger()
logger = logging.getLogger("overflowmod")

# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        main()

        from app import polling
        polling.start()
        
        logger.info("overflowmod started!")

        return super().on_app_running()

    def on_app_shutdown_complete(self):
        from app import db

        db.close()
        logger.debug("[INFO] Database closed")
        return super().on_app_shutdown_complete()