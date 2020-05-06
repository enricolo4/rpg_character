from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class Character:
    player_id: str
    name: str
    race: str
    life: int
    strength: int
    dexterity: int
    intelligence: int
    charisma: int
    wisdom: int
    constitution: int
    id: Optional[UUID] = None
