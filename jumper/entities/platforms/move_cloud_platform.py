import pygame
from jumper.entities.platforms.move_platform import MovePlatform
from jumper.resource import R

class MoveCloudPlatform(MovePlatform):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.image = pygame.transform.scale(R.get_image("platform2"), self.size.int()).convert_alpha()

    def active(self):
        if self.is_touchable and self.is_alive:
            self.environment.player.jump(v=1500)
            self.destroy()

