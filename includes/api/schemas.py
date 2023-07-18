import dataclasses
import datetime
from typing import Optional, List

import arrow as arrow


@dataclasses.dataclass
class GameSchema:
    id: str
    name: str
    min_players: int
    max_players: int
    created: str
    started: Optional[str]


@dataclasses.dataclass
class GameUserSchema:
    id: str
    game: str
    name: str
    created: str


@dataclasses.dataclass
class PlayerListSchema:
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: Optional[List[GameUserSchema]]


@dataclasses.dataclass
class GameTopicSchema:
    id = int
    game: str
    player: str
    label: str
    created: str
