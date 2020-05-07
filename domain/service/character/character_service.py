from domain.model.character import Character
from persitence.character.repository.character_repository import CharacterRepository


class CharacterService:
    def __init__(self):
        self.__character_repository = CharacterRepository()

    def save(self, character: Character) -> Character:
        if character.strength > 100:
            print("TOMA NO CU")

        return self.__character_repository.save(character)
