from core.event.engine import EventSystem
from core.polling.engine import Polling
from core.cache.player_cache import PlayerCache
from core.database.db import Database
from player.repository import PlayerRepository
from player.service import PlayerService

event = EventSystem()
polling = Polling()

pcache = PlayerCache()
db = Database()
prepository = PlayerRepository(database=db)
pservice = PlayerService(
    repository=prepository,
    cache=pcache
)