from domain.model.character import Character
from persitence.character.dbo.character_dbo import CharacterDBO, character_to_dbo


class CharacterRepository:
    def save(self, character: Character) -> Character:
        character_converted_to_dbo: CharacterDBO = character_to_dbo(character)
        character_dbo = self.__save_sql_alchemy(character_converted_to_dbo)
        return character_dbo.to_model()

    def __save_sql_alchemy(self, character_dbo: CharacterDBO) -> CharacterDBO:
        return character_dbo
