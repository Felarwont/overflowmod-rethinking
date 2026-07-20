from app import event
from event.types import PlayerConnectEvent

@event.subscribe(PlayerConnectEvent)
def on_connect(event: PlayerConnectEvent):
    print(f"[CONNECT] player {event.player} connected")