import logging

from app import event_bus, prepository
from overflowmod.src.core.event.types import PlayerDiedEvent

logger = logging.getLogger("overflowmod")

@event_bus.subscribe(PlayerDiedEvent)
def on_death(event: PlayerDiedEvent):
    event.player.add_death()
    prepository.update(event.player)

    if event.killer:
        event.killer.add_kill() # TODO: Добавить транзакцию
        prepository.update(event.killer)

@event_bus.subscribe(PlayerDiedEvent)
def log(event: PlayerDiedEvent):
    if event.killer:
        logger.debug("The player %s passed away by %s", event.player.account_name, event.killer.account_name)
    else:
        logger.debug("The player %s passed away", event.player.account_name)