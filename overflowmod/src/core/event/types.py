from dataclasses import dataclass

from overflowmod.src.players.models import ServerPlayer
from overflowmod.src.core.roster import PlayerSpec

class Event:
    pass

@dataclass(slots=True, frozen=True)
class InternalPlayerConnectEvent(Event):
    player: PlayerSpec

@dataclass(slots=True, frozen=True)
class PlayerConnectEvent(Event):
    player: ServerPlayer

@dataclass(slots=True, frozen=True)
class PlayerDisconnectEvent(Event):
    player: ServerPlayer

@dataclass(slots=True, frozen=True)
class PlayerDiedEvent(Event):
    player: ServerPlayer
    killer: ServerPlayer | None