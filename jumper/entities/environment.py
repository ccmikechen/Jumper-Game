from pygame import Surface
from jumper.entity import Entity
from jumper.entities.player import Player
from jumper.stages.stage1 import Stage1

class Environment(Entity):
    def __init__(self, scene):
        self.scene = scene
        self.stage = Stage1(self)
        self.player = Player(self, (200, 200))
        self.level = 0.0

    def player_jump(self):
        self.player.jump()

    def player_start_moving_left(self):
        self.player.start_moving_left()

    def player_start_moving_right(self):
        self.player.start_moving_right()

    def player_stop_moving_left(self):
        self.player.stop_moving_left()

    def player_stop_moving_right(self):
        self.player.stop_moving_right()

    def get_scene(self):
        return self.scene

    def get_level(self):
        return self.level

    def update(self, delta):
        for p in self.stage.get_platforms():
            p.update(delta)
        self.player.update(delta)

        self._check_player(delta)

    def render(self, screen):
#        background = pygame.transform.scale(R.get_image("dirt"), self.game.get_bound())
#        screen.blit(background, (0, 0))
        screen.fill(self.stage.get_background())

        for p in self.stage.get_platforms():
            p.render(screen)

        self.player.render(screen)

    def _check_player(self, delta):
        for p in self.stage.get_platforms():
            if self.player.get_v() <= 0:
                if self.player.is_on(p):
                    self.player.get_position().y = p.top()
                    self.player.jump()
                    break
