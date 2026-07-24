from core.event.engine import EventSystem
from core.polling.engine import Polling
from core.cache.player_cache import PlayerCache
from core.database.db import Database
from player.repository import PlayerRepository

event = EventSystem()
polling = Polling()

pcache = PlayerCache()
db = Database()
repository = PlayerRepository(database=db)