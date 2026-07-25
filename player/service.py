from .repository import PlayerRepository
from core.cache.player_cache import PlayerCache
from player.models import ServerPlayer
from core.roster import PlayerSpec
from .exception import PlayerAlreadyExist

class PlayerService:
    def __init__(self,
                 repository: PlayerRepository,
                 cache: PlayerCache
                 ):
        self.repository = repository
        self.cache = cache

    def get(self, account_id: str, use_db: bool = False) -> ServerPlayer | None:
        player = self.cache.get(account_id)

        if player:
            return player

        if not use_db:
            return None

        player = self.repository.get(account_id)

        return player

    def handle_connect(self, pspec: PlayerSpec) -> ServerPlayer:
        player = self.get(pspec.account_id, use_db=True)

        if player is None:
            player = ServerPlayer.from_spec(pspec)
            try:
                self.repository.create(player)
                print(f"[INFO] Player {player.account_name} created in database")
            except PlayerAlreadyExist as e:
                print(e)
                raise

        player.client_id = pspec.client_id
        self.cache.add(player)

        return player