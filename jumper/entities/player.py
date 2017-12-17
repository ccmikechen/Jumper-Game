import pygame
from jumper.config import G
from jumper.env_entity import EnvEntity

class Player(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(40, 40)
        self.v = 0
        self.is_moving_left = False
        self.is_moving_right = False

    def jump(self):
        self.v = 1500

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

    def update(self, delta):
        s = 1 / (2 * G * delta)
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

    def render(self, surface):
        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        pygame.draw.rect(surface, (0, 255, 0), (x, y, w, h))
