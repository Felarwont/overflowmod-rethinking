import logging

from app import polling, event_bus, pservice
from overflowmod.src.core.event.types import InternalPlayerConnectEvent, PlayerDisconnectEvent
from overflowmod.src.core import roster

logger = logging.getLogger("overflowmod")

old_account_ids = set()

@polling.every(0.5)
def check_lifecycle() -> None:
    global old_account_ids

    current_acc_ids = {player_spec.account_id for player_spec in roster.get_players_spec()}

    joined = current_acc_ids.difference(old_account_ids)
    left = old_account_ids.difference(current_acc_ids)

    for account_id in joined:
        pspec = roster.get_player_spec(account_id)
        event_bus.emit(InternalPlayerConnectEvent(pspec))
    
    for account_id in left:
        player = pservice.get(account_id)
        if player:
            event_bus.emit(PlayerDisconnectEvent(player))
        # else:
        #     logger.error("The player was not found in the cache when exiting")
    
    old_account_ids = current_acc_ids