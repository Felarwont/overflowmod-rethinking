from app import event
from event.types import PlayerDisconnectEvent

@event.subscribe(PlayerDisconnectEvent)
def on_connect(event: PlayerDisconnectEvent):
    print(f"[DISCONNECT] player {event.player} disconnected")