from core.roster import PlayerSpec

class ServerPlayer:
    def __init__(self,
                 account_id: str,
                 account_name: str,
                 kills: int = 0,
                 deaths: int = 0
                 ):
        self.account_id = account_id
        self.account_name = account_name
        self.kills = kills
        self.deaths = deaths

    def add_kill(self) -> None:
        self.kills += 1

    def add_death(self) -> None:
        self.deaths += 1

    @classmethod
    def from_spec(cls, pspec: PlayerSpec):
        return cls(
            account_id=pspec.account_id,
            account_name=pspec.account_name
        )