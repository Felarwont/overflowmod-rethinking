from core.roster import PlayerSpec

class PlayerCache:
    def __init__(self):
        self.players: dict[str, PlayerSpec] = dict()
    
    def append(self, pspec: PlayerSpec) -> None:
        self.players[pspec.account_id] = pspec
    
    def remove(self, account_id: str) -> PlayerSpec:
        pspec = self.players.pop(account_id)

        if pspec is None:
            pass

        return pspec
    
    def get(self, account_id: str) -> PlayerSpec | None:
        return self.players.get(account_id)
