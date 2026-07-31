import logging

import bascenev1 as bs

from app import event_bus, pservice
from overflowmod.src.core.event.types import InternalPlayerConnectEvent, PlayerConnectEvent
from overflowmod.src.players.exception import PlayerAlreadyExist

logger = logging.getLogger("overflowmod")

@event_bus.subscribe(InternalPlayerConnectEvent)
def on_internal_connect(event: InternalPlayerConnectEvent):
    try:
        player = pservice.handle_connect(event.player)
    except PlayerAlreadyExist as e:
        logger.error("The player %s couldn't be registered in the database: player already exist", e.account_id)
        bs.broadcastmessage(
            "Попробуйте позже...",
            clients=[event.player.client_id],
            color=(1.0, 0.8, 0),
            transient=True
        )
        bs.disconnect_client(event.player.client_id, 1)
    else:
        event_bus.emit(PlayerConnectEvent(player))

@event_bus.subscribe(PlayerConnectEvent)
def on_connect(event: PlayerConnectEvent):
    logger.info("Player connected: %s (%s)", event.player.account_name, event.player.client_id)