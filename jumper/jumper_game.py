import pygame
from jumper.game import Game
from jumper.scenes.home_scene import HomeScene
from jumper.scenes.menu_scene import MenuScene
from jumper.scenes.game_scene import GameScene

class JumperGame(Game):
    def __init__(self):
        super().__init__(title='Jumper Game',
                         window_size=(700, 960),
                         fps=60)

        self.register_scene(HomeScene, "home")
        self.register_scene(MenuScene, "menu")
        self.register_scene(GameScene, "game")

    def start(self):
        self.current_scene = self.scenes_manager.get_scene_by_name("home")
        super().start()
