import logging
import bascenev1 as bs

from app import event, pservice
from core.event.types import InternalPlayerConnectEvent, PlayerConnectEvent
from player.exception import PlayerAlreadyExist

logger = logging.getLogger("overflowmod")

@event.subscribe(InternalPlayerConnectEvent)
def on_internal_connect(event_obj: InternalPlayerConnectEvent):
    try:
        player = pservice.handle_connect(event_obj.player)
    except PlayerAlreadyExist:
        logger.error("The player %s couldn't be registered in the database: player already exist", event_obj.player.account_id)
        bs.broadcastmessage(
            "Попробуйте позже...",
            clients=[event_obj.player.client_id],
            color=(1.0, 0.8, 0),
            transient=True
        )
        bs.disconnect_client(event_obj.player.client_id, 1)
    else:
        event.emit(PlayerConnectEvent(player))

@event.subscribe(PlayerConnectEvent)
def on_connect(event_obj: PlayerConnectEvent):
    logger.info("Player connected: %s (%s)", event_obj.player.account_name, event_obj.player.client_id)