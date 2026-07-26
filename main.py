# ba_meta require api 9
import babase

from app import polling, db

def load_handlers():
    from player import handlers
    from core.polling import pollings

def main():
    load_handlers()


# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        polling.start()
        
        main()
        print("overflowmod started!")

        return super().on_app_running()

    def on_app_shutdown_complete(self):
        db.close()
        print("[INFO] Database closed")
        return super().on_app_shutdown_complete()