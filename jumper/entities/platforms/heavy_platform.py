import pygame
from jumper.entities.platform import Platform
from jumper.resource import R

class HeavyPlatform(Platform):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.image = pygame.transform.scale(R.get_image("platform3"), self.size.int())

    def get_color(self):
        return (0, 128, 255)

    def active(self):
        if self.is_touchable and self.is_alive:
            self.environment.player.jump(v=1200)
