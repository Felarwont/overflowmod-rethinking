import logging

from .repository import PlayerRepository
from overflowmod.src.players.models import ServerPlayer
from overflowmod.src.core.roster import PlayerSpec

logger = logging.getLogger("overflowmod")

class PlayerService:
    def __init__(self, repository: PlayerRepository):
        self.repository = repository

    def get(self, account_id: str) -> ServerPlayer | None:    # TODO: Добавить поиск по OnlineManager
        return self.repository.get(account_id)

    def handle_connect(self, pspec: PlayerSpec) -> ServerPlayer:
        player = self.get(pspec.account_id)

        if player is None:
            player = ServerPlayer.from_spec(pspec)
            self.repository.create(player)
            logger.info("Player %s created in database", player.account_name)

        player.client_id = pspec.client_id    # TODO: Перенести это свойство в OnlinePlayer

        return player

    def handle_disconnect(self, player: ServerPlayer) -> None:
        self.repository.update(player)