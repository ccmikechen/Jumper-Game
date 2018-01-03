import pygame
from jumper.resource import R
from random import randint
from math import sqrt
from jumper.scene import Scene
from jumper.entities.environment import Environment

UPDATE_RATE = 0.01

class GameScene(Scene):
    def setup(self):
        self.environment = None

    def reset(self, params={}):
        self.is_running = True
        self.game_status = None
        self.last_delta = 0.0

        stage = params["stage"] if "stage" in params else None
        self.environment = Environment(self, stage)

    def update(self, delta):
        if not self.is_running:
            return

        self.last_delta += delta

        while self.last_delta >= UPDATE_RATE:
            self.last_delta -= UPDATE_RATE
            self.environment.update(UPDATE_RATE)
            super().update(UPDATE_RATE)

    def render(self, screen):
        screen.fill((0, 0, 0))

        if self.game_status != None:
            if self.game_status.status == GAME_OVER:
                self._show_winner_message(screen, self.game_status.winner)
            elif self.game_status.status == DRAW:
                self._show_draw_message(screen)

        self.environment.render(screen)
        super().render(screen)

    def on_key_down(self, key):
        if not self.environment.is_pause:
            if key == pygame.K_SPACE:
                self.environment.player_attack()
            if key == pygame.K_j:
                self.environment.player_jump()
            if key == pygame.K_LEFT:
                self.environment.player_start_moving_left()
            if key == pygame.K_RIGHT:
                self.environment.player_start_moving_right()

        if key == pygame.K_p:
            self.environment.toggle_pause()

        self.environment.key_down(key)

    def on_key_up(self, key):
        if key == pygame.K_LEFT:
            self.environment.player_stop_moving_left()
        if key == pygame.K_RIGHT:
            self.environment.player_stop_moving_right()

        self.environment.key_up(key)

class GameStatus:
    def __init__(self, status, winner=None, loser=None):
        self.status = status
        self.winner = winner
        self.loser = loser
