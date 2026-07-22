from app import event, pcache
from core.event.types import PlayerConnectEvent

@event.subscribe(PlayerConnectEvent)
def on_connect(event: PlayerConnectEvent):
    pcache.append(event.player)
    print(f"[INFO] Player connected: {event.player.account_name}")