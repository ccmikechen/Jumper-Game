import pygame
from jumper.entities.platform import Platform
from jumper.resource import R

class MovePlatform(Platform):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.image = pygame.transform.scale(R.get_image("platform1"), self.size.int())

        self.direction = 1
        self.progress = 0.0
        self.speed = 100

    def get_color(self):
        return (0, 128, 255)

    def active(self):
        if self.is_touchable and self.is_alive:
            self.environment.player.jump(v=1500)

    def update(self, delta):
        bw, bh = self.environment.get_scene().get_bound()
        progress = self._get_next_progress(delta)
        next_x = self._get_next_x(delta)

        if (abs(progress) > 2.0) or (next_x < 0) or ((next_x + self.size.w) > bw):
            self.direction *= -1
            self.progress = self._get_next_progress(delta)
        else:
            self.progress = progress

        self.position.x = self._get_next_x(delta)

    def _get_next_progress(self, delta):
        return self.progress + delta * self.direction

    def _get_next_x(self, delta):
        return self.position.x + (delta * self.speed) * self.direction
