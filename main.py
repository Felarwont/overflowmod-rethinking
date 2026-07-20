# ba_meta require api 9
import babase

from app import updater

def main():
    from player import handlers


# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        self.timer = babase.AppTimer(0.5, updater.update, True)
        
        main()