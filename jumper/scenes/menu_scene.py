import pygame
from jumper.resource import R
from jumper.scene import Scene
from jumper.entities.ui.stage_selector import StageSelector
from jumper.db.database import Database

class MenuScene(Scene):
    def setup(self):
        db = Database()
        stages = db.get_stages()

        self.selector = StageSelector(stages, (100, 200), 480)

        self.background = R.get_image("menu_bg")

    def update(self, delta):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0), (400, 0) + self.get_bound())

        self.selector.render(screen)

    def on_key_down(self, key):
        if key == pygame.K_DOWN:
            self.selector.next()
        if key == pygame.K_UP:
            self.selector.prev()
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            self.select_stage(self.selector.get_selected_stage())
        if key == pygame.K_BACKSPACE:
            self.start_scene("home")

    def select_stage(self, stage):
        self.start_and_reset_scene("game", params={"stage": stage})
