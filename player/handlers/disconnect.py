from app import event, pservice
from core.event.types import PlayerDisconnectEvent

@event.subscribe(PlayerDisconnectEvent)
def on_connect(event_obj: PlayerDisconnectEvent):
    pservice.handle_disconnect(event_obj.player)

    print(f"[INFO] Player disconnected: {event_obj.player.account_name} ({event_obj.player.client_id})")