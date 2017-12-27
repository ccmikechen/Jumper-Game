import pygame
from jumper.config import config
from jumper.env_entity import EnvEntity

class Player(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(40, 40)
        self.v = 0
        self.is_moving_left = False
        self.is_moving_right = False
        self.items = []

    def jump(self, v=1500):
        self.v = v

        for item in self.items:
            item.on_jump(self)

    def start_moving_left(self):
        self.is_moving_left = True

    def start_moving_right(self):
        self.is_moving_right = True

    def stop_moving_left(self):
        self.is_moving_left = False

    def stop_moving_right(self):
        self.is_moving_right = False

    def get_v(self):
        return self.v

    def pos(self):
        return self.position

    def add_item(self, new_item):
        for item in self.items:
            if item.get_name() == new_item.get_name():
                item.reactive(self)
                return

        new_item.reactive(self)
        self.items.append(new_item)

    def remove_item(self, item):
        for i in range(0, len(self.items)):
            if self.items[i].get_name() == item.get_name():
                del self.items[i]
                return
        print(self.items)

    def update(self, delta):
        s = 1 / (2 * config.G * delta)
        self.v -= s
        self.position.y += self.v * delta

        (env_width, env_height) = self.environment.get_scene().get_bound()

        if self.is_moving_left:
            self.position.x -= delta * 1000
            if self.right() <= 0:
                self.position.x += env_width
        if self.is_moving_right:
            self.position.x += delta * 1000
            if self.left() >= env_width:
                self.position.x -= env_width

    def render(self, surface, camera):
        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        pygame.draw.rect(surface, (0, 255, 0), (x, y + camera, w, h))
