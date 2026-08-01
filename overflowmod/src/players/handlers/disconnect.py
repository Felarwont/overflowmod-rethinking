import logging

from app import event_bus, pservice
from overflowmod.src.core.event.types import PlayerDisconnectEvent

logger = logging.getLogger("overflowmod")

@event_bus.subscribe(PlayerDisconnectEvent)
def on_connect(event: PlayerDisconnectEvent):
    pservice.handle_disconnect(event.player)

    logger.debug("Player disconnected: %s (%s)", event.player.account_name, event.player.client_id)