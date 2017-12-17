import pygame
from jumper.config import G
from jumper.env_entity import EnvEntity

class Player(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(40, 40)
        self.v = 0

    def jump(self):
        self.v = 1500

    def update(self, delta):
        s = 1 / (2 * G * delta)
        self.v -= s
        self.position.y += self.v * delta

    def render(self, surface):
        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        pygame.draw.rect(surface, (0, 255, 0), (x, y, w, h))
