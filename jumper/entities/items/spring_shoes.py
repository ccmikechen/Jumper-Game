import pygame
from jumper.entities.item import Item
from jumper.resource import R

class SpringShoes(Item):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'Sprint shoes')
        self.image = pygame.transform.scale(R.get_image("spring_shoes"), self.size.int())

    def get_color(self):
        return (0, 255, 0)

    def render(self, surface, camera):
        super().render(surface, camera)

    def active(self, player):
        super().active(player)

    def reactive(self, player):
        self.count = 6

    def on_jump(self, player):
        player.v = 2500
        self.count -= 1

        if self.count <= 0:
            self.destory(player)
