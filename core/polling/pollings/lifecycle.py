from app import polling, event, pcache
from core.event.types import PlayerConnectEvent, PlayerDisconnectEvent
import core.roster as roster
from player.models import ServerPlayer

old_account_ids = set()

@polling.every(0.5)
def check_lifecycle() -> None:
    global old_account_ids

    current_acc_ids = {player_spec.account_id for player_spec in roster.get_players_spec()}

    joined = current_acc_ids.difference(old_account_ids)
    left = old_account_ids.difference(current_acc_ids)

    for account_id in joined:
        pspec = roster.get_player_spec(account_id)
        event.emit(PlayerConnectEvent(ServerPlayer.from_spec(pspec)))
    
    for account_id in left:
        pspec = pcache.get(account_id)
        if pspec is None:
            raise KeyError("Игрок не найден в кэше.")
        event.emit(PlayerDisconnectEvent(ServerPlayer.from_spec(pspec)))
    
    old_account_ids = current_acc_ids