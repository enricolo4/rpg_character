import uuid
from dataclasses import dataclass
from typing import Optional

from domain.model.character import Character
from domain.model.player import Player


@dataclass
class CharacterDTO:
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
    id: Optional[str] = None

    @property
    def to_model(self) -> Character:
        return Character(
            id=self.id,
            player_id=self.player_id,
            name=self.player_id,
            race=self.race,
            life=self.life,
            strength=self.strength,
            dexterity=self.dexterity,
            intelligence=self.intelligence,
            charisma=self.charisma,
            wisdom=self.wisdom,
            constitution=self.constitution
        )


def character_to_dto(character: Character) -> CharacterDTO:
    return CharacterDTO(
        id=str(character.id),
        player_id=character.player_id,
        name=character.player_id,
        race=character.race,
        life=character.life,
        strength=character.strength,
        dexterity=character.dexterity,
        intelligence=character.intelligence,
        charisma=character.charisma,
        wisdom=character.wisdom,
        constitution=character.constitution
    )
