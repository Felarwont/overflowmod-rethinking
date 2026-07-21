from app import event, pcache
from event.types import PlayerDisconnectEvent

@event.subscribe(PlayerDisconnectEvent)
def on_connect(event: PlayerDisconnectEvent):
    pcache.remove(event.player.account_id)
    print(f"[INFO] Player disconnected: {event.player.account_name}")