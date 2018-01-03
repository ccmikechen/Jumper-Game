import pygame
from jumper.entities.item import Item
from jumper.resource import R

class Coin(Item):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'Coin')
        self.image = pygame.transform.scale(R.get_image("coin"), self.size.int())



