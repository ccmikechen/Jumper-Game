import pygame
from jumper.entities.bullet import Bullet
from math import pi, sin, cos

class BBWaveBullet(Bullet):
    def __init__(self, environment, position, angle, speed=1000):
        super().__init__(environment, position)

        self.speed = speed
        self.angle = angle
        self.wave_acc = 0.0
        self.set_size(20, 20)

    def update(self, delta):
        if not self.is_alive:
            return

        self.wave_acc = (self.wave_acc + self.speed * delta) % 360
        wave_angle = sin(self.wave_acc / 180 * pi) * 40

        x = self.position.x + self.speed * delta * cos((self.angle + wave_angle) / 180 * pi)
        y = self.position.y + self.speed * delta * sin((self.angle + wave_angle) / 180 * pi)

        camera = self.environment.camera
        (bound_x, bound_y) = self.environment.scene.get_bound()

        if (x < 0 or x > bound_x) or (y > bound_y + camera.pos() or y < 0):
            self.destory()
        else:
            self.set_position(x, y)

    def render_bullet(self, surface, position):
        (w, h) = self.get_size().int()
        (x, y) = int(position[0] + w/2), int(position[1] + h/2)
        r = int(w/2)

        for i in range(0, r, 2):
            radius = r - i
            c = 255 - 10 * i
            pygame.draw.circle(surface, (0, c, c), (x, y), radius)

    def get_color(self):
        return (0, 255, 255)
