import pygame
from jumper.env_entity import EnvEntity
from math import sin, pi
from random import randint

class Item(EnvEntity):
    def __init__(self, environment, position, name):
        super().__init__(environment, position)
        self.set_size(50, 50)
        self.name = name
        self.image = None
        environment.counter.inc_item_appear(self.get_name())
        self.effect_acc = randint(0, 360)
        self.effect_offset = 0.0
        self.effect_speed = 200

    def update(self, delta):
        self.effect_acc = (self.effect_acc + self.effect_speed * delta) % 360
        self.effect_offset = sin(self.effect_acc / 180 * pi) * 8 + 8

    def render(self, surface, camera):
        if not self.is_visible:
            return

        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        if self.get_image() == None:
            pygame.draw.rect(surface, self.get_color(), (x, y + camera, w, h))
        else:
            surface.blit(self.get_image(), (x, y + camera - self.effect_offset))

    def get_color(self):
        return (0, 0, 0)

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name

    def get_type(self):
        return 'item'

    def active(self, player):
        player.add_item(self)
        self.is_touchable = False
        self.is_visible = False
        self.environment.counter.inc_item_active(self.get_name())

    def reactive(self, player):
        pass

    def destory(self, player):
        super().destroy()

        player.remove_item(self)

    def on_jump(self, player):
        pass

    def on_drop(self, player):
        pass

    def on_attack(self, player):
        pass
