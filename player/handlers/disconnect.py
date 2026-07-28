import logging

from app import event, pservice
from core.event.types import PlayerDisconnectEvent

logger = logging.getLogger("overflowmod")

@event.subscribe(PlayerDisconnectEvent)
def on_connect(event_obj: PlayerDisconnectEvent):
    pservice.handle_disconnect(event_obj.player)

    logger.info("Player disconnected: %s (%s)", event_obj.player.account_name, event_obj.player.client_id)