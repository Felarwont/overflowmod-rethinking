from dataclasses import dataclass

class Event:
    pass

@dataclass(slots=True, frozen=True)
class PlayerConnectEvent(Event):
    player: str

@dataclass(slots=True, frozen=True)
class PlayerDisconnectEvent(Event):
    player: str

@dataclass(slots=True, frozen=True)
class PlayerDiedEvent(Event):
    player: str
    killer: str | None