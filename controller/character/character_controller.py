import json

from falcon import Request, Response

from controller.character.dto.character_dto import CharacterDTO, character_to_dto
from domain.model.character import Character
from domain.service.character.character_service import CharacterService


class CharacterController:
    def __init__(self):
        self.__character_service = CharacterService()

    def on_post(self, request: Request, response: Response):
        character_dto = CharacterDTO(**request.media)
        character: Character = self.__character_service.save(character_dto.to_model)
        response.body = json.dumps(character_to_dto(character).__dict__)
