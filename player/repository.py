import logging
from sqlite3 import IntegrityError

from core.database.db import Database
from core.database.models import Players
from player.models import ServerPlayer
from .exception import PlayerAlreadyExist

logger = logging.getLogger("overflowmod")

class PlayerRepository:
    def __init__(self, database: Database):
        self.db = database
        self.db.create_table(Players)

    def create(self, player: ServerPlayer) -> None:
        try:
            self.db.execute(
                """
                INSERT INTO players (account_id, account_name, kills, deaths)
                VALUES (?, ?, ?, ?);
                """,
                (
                    player.account_id,
                    player.account_name,
                    player.kills,
                    player.deaths,
                )
            )
        except IntegrityError:
            raise PlayerAlreadyExist(player.account_id)

    def get(self, account_id: str) -> ServerPlayer | None:
        db_player = self.db.fetch_one(
            """
            SELECT
                account_id,
                account_name,
                kills,
                deaths
            FROM players
            WHERE account_id = ?;
            """,
            (account_id,)
        )

        if db_player is None:
            return None

        return ServerPlayer(*db_player)

    def update(self, player: ServerPlayer) -> None:
        rowcount = self.db.execute(
            """
            UPDATE players
            SET account_name = ?,
                kills = ?,
                deaths = ?
            WHERE account_id = ?
            """,
            (
                player.account_name,
                player.kills,
                player.deaths,
                player.account_id,
            )
        )

        if rowcount != 1:
            logger.warning("Player %s / %s couldn't be updated", player.client_id, player.account_name)