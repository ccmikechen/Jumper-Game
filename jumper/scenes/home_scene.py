import pygame
from jumper.resource import R
from jumper.scene import Scene
from jumper.entity import Entity
from jumper.entities.information import Information
from math import sin, cos, pi, atan2
from random import randint

class HomeScene(Scene):
    def setup(self):
        self.background = Background(R.get_image("home_bg"), self.get_bound())
        self.information_ui = Information()

    def update(self, delta):
        self.background.update(delta)
        self.information_ui.update(delta)

    def render(self, screen):
        screen.fill((0, 0, 0))

        self.background.render(screen)
        self.information_ui.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            self.start_and_reset_scene("menu")

class Background(Entity):
    def __init__(self, image, size):
        self.position = (0, 0)
        self.speed = 100
        self.image = image
        self.size = size

        (w, h) = self.image.get_rect().size
        self.g_pos = (randint(0, w), randint(0, h))
        self.g_angle = randint(0, 360)
        self.g_speed = 1000

    def update(self, delta):
        w, h = self.image.get_rect().size
        g_x = self.g_pos[0] + self.g_speed * delta * cos(self.g_angle / 180 * pi)
        g_y = self.g_pos[1] + self.g_speed * delta * sin(self.g_angle / 180 * pi)

        if g_x < 0 or g_x >= w or g_y < 0 or g_y > h:
            self.g_angle = randint(0, 360)
            self.update(delta)
            return
        else:
            self.g_pos = (g_x, g_y)

        angle = atan2(g_y - self.position[1], g_x - self.position[0])
        x = self.position[0] + self.speed * delta * cos(angle)
        y = self.position[1] + self.speed * delta * sin(angle)

        self.position = (max(0, min(w - self.size[0], x)), max(0, min(h - self.size[1], y)))

    def render(self, surface):
        surface.blit(self.image, (0, 0), (self.position + self.size))
