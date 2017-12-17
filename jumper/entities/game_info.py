from jumper.entity import Entity
from jumper.game_helper import show_text

WHITE = (255, 255, 255)

class GameInfo(Entity):
    def __init__(self, bound):
        self.bound = bound

    def update(self, delta, params):
        pass

    def render(self, screen):
        pass
