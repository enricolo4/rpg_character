import falcon
from waitress import serve

from controller.character.character_controller import CharacterController
from controller.health.health_controller import HealthController

application = falcon.API()

application.add_route("/health", HealthController())
application.add_route("/character", CharacterController())

