import pygame
from jumper.entities.item import Item
from jumper.timer import Timer
from jumper.config import config
from jumper.resource import R

class GravityReducer(Item):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'Gravity Reducer')
        self.timer = Timer()
        self.image = pygame.transform.scale(R.get_image("gravity_reducer"), self.size.int())

    def get_color(self):
        return (255, 0, 0)

    def render(self, surface, camera):
        super().render(surface, camera)

    def active(self, player):
        self.player = player
        super().active(player)

    def reactive(self, player):
        config.G = 5.0
        self.timer.restart()

    def update(self, delta):
        if not self.is_alive:
            return

        self.timer.update()

        if self.timer.get_time() > 10:
            config.reset_G()
            self.destory(self.player)
