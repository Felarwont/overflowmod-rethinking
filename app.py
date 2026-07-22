from core.event.engine import EventSystem
from core.polling.engine import Polling
from player.cache import PlayerCache

event = EventSystem()
polling = Polling()

pcache = PlayerCache()