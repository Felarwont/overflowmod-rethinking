class GameBaseModel:
    pass

class Players(GameBaseModel):
    id: int
    account_id: str
    account_name: str
    kills: int
    deaths: int

    @staticmethod
    def create_query():
        return """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id TEXT NOT NULL UNIQUE,
                account_name TEXT NOT NULL,
                kills INTEGER NOT NULL DEFAULT 0 CHECK (kills >= 0),
                deaths INTEGER NOT NULL DEFAULT 0 CHECK (deaths >= 0)
            );
            """