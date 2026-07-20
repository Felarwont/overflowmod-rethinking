from app import updater, event
from event.types import PlayerConnectEvent, PlayerDisconnectEvent
import roster

old_account_ids = set()

@updater.every(0.5)
def check_lifecycle() -> None:
    global old_account_ids

    current_acc_ids = {player_spec.account_id for player_spec in roster.get_players_spec()}

    joined = current_acc_ids.difference(old_account_ids)
    left = old_account_ids.difference(current_acc_ids)

    for account_id in joined:
        name = roster.get_player_spec(account_id).account_name
        event.emit(PlayerConnectEvent(name))
    
    for account_id in left:
        print("Disconnect")
        # name = roster.get_player_spec(account_id).account_name
        # event.emit(PlayerDisconnectEvent(name))
    
    old_account_ids = current_acc_ids