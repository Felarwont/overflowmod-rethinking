# ba_meta require api 9
import babase

from app import polling

def main():
    from player import handlers
    from polling import pollings


# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        polling.start()
        
        main()

        print("overflowmod started!")