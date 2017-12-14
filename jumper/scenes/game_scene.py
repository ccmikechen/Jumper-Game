import pygame
from jumper.resource import R
from random import randint
from math import sqrt
from jumper.scene import Scene

class GameScene(Scene):
    def setup(self):
        self.reset()
#        self.game_info = GameInfo(self.game.get_bound())

    def reset(self):
        self.is_running = True
        self.game_status = None

    def update(self, delta):
        if self.is_running:
            pass
        super().update(delta)

    def render(self, screen):
        screen.fill((0, 0, 0))

#        background = pygame.transform.scale(R.get_image("dirt"), self.game.get_bound())
#        screen.blit(background, (0, 0))

        if self.game_status != None:
            if self.game_status.status == GAME_OVER:
                self._show_winner_message(screen, self.game_status.winner)
            elif self.game_status.status == DRAW:
                self._show_draw_message(screen)

        self.game_info.render(screen)
        super().render(screen)

    def on_key_down(self, key):
        if key == pygame.K_SPACE:
            if not self.is_running:
                self.reset()
        if key == pygame.K_BACKSPACE:
            self.start_scene("menu")
        if key == pygame.K_z:
            self.player_1.add_snake_length(10)
        if key == pygame.K_x:
            self.player_2.add_snake_length(10)
        if key == pygame.K_d:
            self.player_1.is_turning_right = True
        if key == pygame.K_a:
            self.player_1.is_turning_left = True
        if key == pygame.K_l:
            self.player_2.is_turning_right = True
        if key == pygame.K_j:
            self.player_2.is_turning_left = True

    def on_key_up(self, key):
        if key == pygame.K_d:
            self.player_1.is_turning_right = False
        if key == pygame.K_a:
            self.player_1.is_turning_left = False
        if key == pygame.K_l:
            self.player_2.is_turning_right = False
        if key == pygame.K_j:
            self.player_2.is_turning_left = False

class GameStatus:
    def __init__(self, status, winner=None, loser=None):
        self.status = status
        self.winner = winner
        self.loser = loser
