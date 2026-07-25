from app import event, pservice
from core.event.types import InternalPlayerConnectEvent, PlayerConnectEvent

@event.subscribe(InternalPlayerConnectEvent)
def on_internal_connect(event_obj: InternalPlayerConnectEvent):
    player = pservice.handle_connect(event_obj.player)

    event.emit(PlayerConnectEvent(player))

@event.subscribe(PlayerConnectEvent)
def on_connect(event_obj: PlayerConnectEvent):
    print(f"[INFO] Player connected: {event_obj.player.account_name} ({event_obj.player.client_id})")