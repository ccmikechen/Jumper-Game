import pygame
from jumper.env_entity import EnvEntity

class Platform(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(100, 30)

    def update(self, delta):
        pass

    def render(self, surface):
        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        pygame.draw.rect(surface, self.get_color(), (x, y, w, h))

    def get_color(self):
        return (0, 0, 255)

    def active(self):
        pass
