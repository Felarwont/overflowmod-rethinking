# ba_meta require api 9
import babase

from app import updater

def main():
    from player import handlers
    from updater import pollings


# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        self.timer = babase.AppTimer(0.2, updater.update, True)
        
        main()

        print("overflowmod started!")