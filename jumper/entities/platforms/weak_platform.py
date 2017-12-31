import pygame
from jumper.entities.platform import Platform
from jumper.resource import R

class WeakPlatform(Platform):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.image = pygame.transform.scale(R.get_image("platform1"), self.size.int()).convert_alpha()
        self.image.fill((255, 255, 255, 120), None, pygame.BLEND_RGBA_MULT)

    def get_color(self):
        return (0, 128, 128)

    def active(self):
        if self.is_touchable and self.is_alive:
            self.destroy()
