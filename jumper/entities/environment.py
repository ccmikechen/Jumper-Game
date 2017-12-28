from pygame import Surface
from jumper.entity import Entity
from jumper.entities.player import Player
from jumper.stages.stage1 import Stage1
from jumper.stages.stage2 import Stage2
from jumper.camera import Camera
from jumper.config import config
from jumper.timer import Timer

DEFAULT_LEVEL = 12

class Environment(Entity):
    def __init__(self, scene, stage=1):
        self.scene = scene
        self.camera = Camera(speed=0.2)
        self.player = Player(self, (200, 200))
        self.timer = Timer()
        self.reset(stage)

    def reset(self, stage=None):
        stage_id = stage[0] if stage != None else 0

        if stage_id == 1:
            self.stage = Stage1(self)
        elif stage_id == 2:
            self.stage = Stage2(self)
        else:
            self.stage = Stage1(self)

        self.timer.restart()
        self.is_game_over = False
        self.level = DEFAULT_LEVEL
        config.reset()

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
        self.timer.update()
        self.stage.update(self.level)
        for p in self.stage.get_platforms():
            p.update(delta)

        for item in self.stage.get_items():
            item.update(delta)

        self.player.update(delta)

        current_level = int(self.player.pos().y / config.LEVEL_HEIGHT)
        if current_level > self.level:
            self.level = current_level

        self.camera.move((self.level - DEFAULT_LEVEL - 2) * config.LEVEL_HEIGHT)
        self.camera.update(delta)

        self.stage.get_info().update(delta, params={
            "level": self.level,
            "time": self.timer.get_time()
        })
        self._check_player(delta)

    def render(self, screen):
#        background = pygame.transform.scale(R.get_image("dirt"), self.game.get_bound())
#        screen.blit(background, (0, 0))
        screen.fill(self.stage.get_background())

        camera_pos = self.camera.pos()

        for p in self.stage.get_platforms():
            p.render(screen, camera_pos)

        for item in self.stage.get_items():
            item.render(screen, camera_pos)

        self.player.render(screen, camera_pos)
        self.stage.get_info().render(screen)

    def _check_player(self, delta):
        if self.player.get_position().y < self.camera.pos():
            self.is_game_over = True
            print('game over')
            return

        self._check_platforms(delta)
        self._check_items(delta)

    def _check_platforms(self, delta):
        for p in self.stage.get_platforms():
            if not p.is_touchable:
                continue

            if self.player.get_v() <= 0:
                if self.player.is_on(p):
                    self.player.get_position().y = p.top()
                    p.active()
                    break

    def _check_items(self, delta):
        for item in self.stage.get_items():
            if not item.is_touchable:
                continue

            if self.player.is_touch(item):
                item.active(self.player)
