from event.engine import EventSystem
from polling.engine import Polling
from player.cache import PlayerCache

event = EventSystem()
polling = Polling()

pcache = PlayerCache()