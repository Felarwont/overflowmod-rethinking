from bascenev1 import Session, broadcastmessage

old_on_player_request = Session.on_player_request
def new_on_player_request(self, sessionplayer):
    if not old_on_player_request(self, sessionplayer):
        return False

    account_id = sessionplayer.get_account_id()
    
    if account_id is None:
        broadcastmessage(
            "Загрузка данных...",
            clients=[sessionplayer.inputdevice.client_id],
            color=(1.0, 0.5, 0.5),
            transient=True
        )
        return False

    for s_player in self.sessionplayers:
        if s_player.get_account_id() == account_id:
            broadcastmessage(
                "Вы уже вошли с этого аккаунта",
                clients=[sessionplayer.inputdevice.client_id],
                color=(1.0, 1.0, 0.5),
                transient=True
            )
            return False

    return True

def apply_session_patches() -> None:
    Session.on_player_request = new_on_player_request