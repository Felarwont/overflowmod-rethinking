from player.models import ServerPlayer

class PlayerCache:
    def __init__(self):
        self.players: dict[str, ServerPlayer] = dict()
    
    def add(self, player: ServerPlayer) -> None:
        self.players[player.account_id] = player
    
    def remove(self, account_id: str) -> ServerPlayer:
        player = self.players.pop(account_id, None)

        if player is None:
            pass

        return player
    
    def get(self, account_id: str) -> ServerPlayer | None:
        return self.players.get(account_id)
