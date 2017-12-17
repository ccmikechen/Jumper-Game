import pygame
from jumper.resource import R
from jumper.scene import Scene
from jumper.entities.information import Information

class MenuScene(Scene):
    def setup(self):
        self.information_ui = Information()

    def update(self, delta):
        self.information_ui.update(delta)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.information_ui.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            self.start_and_reset_scene("game")
