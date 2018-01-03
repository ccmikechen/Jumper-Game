import pygame
from jumper.entities.platforms.move_platform import MovePlatform
from jumper.resource import R

class MoveWeakPlatform(MovePlatform):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.image = pygame.transform.scale(R.get_image("platform1"), self.size.int()).convert_alpha()
        self.image.fill((255, 255, 255, 120), None, pygame.BLEND_RGBA_MULT)

    def active(self):
        if self.is_touchable and self.is_alive:
            self.destroy()
