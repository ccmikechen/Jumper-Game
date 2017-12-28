import pygame
from jumper.resource import R
from jumper.scene import Scene
from jumper.entities.ui.stage_selector import StageSelector
from jumper.db.database import Database

class MenuScene(Scene):
    def setup(self):
        db = Database()
        stages = db.get_stages()

        self.selector = StageSelector(stages, (0, 200), 480)

    def update(self, delta):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.selector.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_DOWN:
            self.selector.next()
        if key == pygame.K_UP:
            self.selector.prev()
        if key == pygame.K_SPACE:
            self.select_stage(self.selector.get_selected_stage())

    def select_stage(self, stage):
        self.start_and_reset_scene("game", params={"stage": stage})
