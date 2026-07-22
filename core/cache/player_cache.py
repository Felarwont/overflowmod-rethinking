from player.models import ServerPlayer

class PlayerCache:
    def __init__(self):
        self.players: dict[str, ServerPlayer] = dict()
    
    def add(self, pspec: ServerPlayer) -> None:
        self.players[pspec.account_id] = pspec
    
    def remove(self, account_id: str) -> ServerPlayer:
        pspec = self.players.pop(account_id)

        if pspec is None:
            pass

        return pspec
    
    def get(self, account_id: str) -> ServerPlayer | None:
        return self.players.get(account_id)
