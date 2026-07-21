from dataclasses import dataclass

from roster import PlayerSpec

class Event:
    pass

@dataclass(slots=True, frozen=True)
class PlayerConnectEvent(Event):
    player: PlayerSpec

@dataclass(slots=True, frozen=True)
class PlayerDisconnectEvent(Event):
    player: PlayerSpec

@dataclass(slots=True, frozen=True)
class PlayerDiedEvent(Event):
    player: PlayerSpec
    killer: PlayerSpec | None