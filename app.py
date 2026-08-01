from overflowmod.src.core.event.engine import EventBus
from overflowmod.src.core.polling.engine import Polling
from overflowmod.src.core.database.db import Database
from overflowmod.src.players.repository import PlayerRepository
from overflowmod.src.players.service import PlayerService

event_bus = EventBus()
polling = Polling()

db = Database()
prepository = PlayerRepository(database=db)
pservice = PlayerService(repository=prepository)