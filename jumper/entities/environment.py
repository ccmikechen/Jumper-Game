import pygame
from jumper.entity import Entity
from jumper.entities.player import Player
from jumper.entities.ui.ranking_frame import RankingFrame
from jumper.stages.stage1 import Stage1
from jumper.stages.stage2 import Stage2
from jumper.camera import Camera
from jumper.config import config
from jumper.timer import Timer
from jumper.game_helper import show_text
from jumper.game_counter import GameCounter
from jumper.db.database import Database

DEFAULT_LEVEL = 12
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Environment(Entity):
    def __init__(self, scene, stage=1):
        self.scene = scene
        self.camera = Camera(speed=0.2)
        self.counter = GameCounter()
        self.player = Player(self, (200, 200))
        self.bullets = []
        self.timer = Timer()
        self.counter = GameCounter()
        self.ranking_frame = RankingFrame(scene, (50, 30))
        self.db = Database()
        self.reset(stage)

    def reset(self, stage=None):
        self.counter.reset()

        stage_id = stage if stage != None else 1

        if stage_id == 1:
            self.stage = Stage1(self)
        elif stage_id == 2:
            self.stage = Stage2(self)

        self.timer.restart()

        self.is_pause = False
        self.is_stop = False
        self.is_game_over = False
        self.is_clear = False

        self.level = DEFAULT_LEVEL
        config.reset()

        self.ranking_frame.hide()

        self.start_counter = StartCounter(self)

    def player_jump(self):
        if self.is_pause or self.is_stop or self.is_clear or self.is_game_over:
            return
        self.player.jump()

    def player_start_moving_left(self):
        if self.is_game_over: return
        self.player.start_moving_left()

    def player_start_moving_right(self):
        if self.is_game_over: return
        self.player.start_moving_right()

    def player_stop_moving_left(self):
        if self.is_game_over: return
        self.player.stop_moving_left()

    def player_stop_moving_right(self):
        if self.is_game_over: return
        self.player.stop_moving_right()

    def player_attack(self):
        if self.is_pause or self.is_stop or self.is_clear or self.is_game_over:
            return

        self.player.attack()

    def add_bullet(self, bullet):
        self.bullets = list(filter(lambda b: b.is_alive, self.bullets))
        self.bullets.append(bullet)

    def get_scene(self):
        return self.scene

    def get_level(self):
        return self.level

    def get_stage(self):
        return self.stage

    def get_next_stage_id(self):
        return self.stage.get_next_stage_id()

    def pause(self, enable=True):
        if self.is_clear or self.is_stop:
            return

        self.is_pause = enable

        if enable:
            self.timer.pause()
        else:
            self.timer.resume()

    def toggle_pause(self):
        self.pause(not self.is_pause)

    def stop(self, enable=True):
        self.is_stop = enable

    def toggle_stop(self):
        self.is_stop = not self.is_stop

    def game_over(self):
        self.is_game_over = True
        self.ranking_frame.disable_next_stage_option()
        self._show_ranking()

    def key_down(self, key):
        if not self.ranking_frame.is_hidden:
            self.ranking_frame.key_down(key)
            return

        if key == pygame.K_BACKSPACE:
            self.scene.start_scene("menu")

    def key_up(self, key):
        if not self.ranking_frame.is_hidden:
            self.ranking_frame.key_up(key)
            return

    def update(self, delta):
        if self.is_clear or self.is_game_over:
            self.ranking_frame.update(delta)
            return

        if self.is_pause or self.is_stop:
            return

        if not self.start_counter.is_finished():
            self.start_counter.update(delta)
            return

        self.timer.update()
        self.stage.update(self.level)

        for p in self.stage.get_platforms():
            p.update(delta)

        for item in self.stage.get_items():
            item.update(delta)

        for m in self.stage.get_monsters():
            m.update(delta)

        for b in self.bullets:
            b.update(delta)

        self.player.update(delta)

        current_level = int(self.player.pos().y / config.LEVEL_HEIGHT)
        if current_level > self.level:
            self.level = current_level

        self.camera.move((self.level - DEFAULT_LEVEL - 2) * config.LEVEL_HEIGHT)
        self.camera.update(delta)

        self.counter.update_level(self.level)
        self.counter.update_time(self.timer.get_time())

        self._check_player(delta)
        self._check_mission()

    def render(self, screen):
#        background = pygame.transform.scale(R.get_image("dirt"), self.game.get_bound())
#        screen.blit(background, (0, 0))
        screen.fill(BLACK)

        camera_pos = self.camera.pos()

        self._render_background(screen)

        for p in self.stage.get_platforms():
            p.render(screen, camera_pos)

        for item in self.stage.get_items():
            item.render(screen, camera_pos)

        for m in self.stage.get_monsters():
            m.render(screen, camera_pos)

        for b in self.bullets:
            b.render(screen, camera_pos)

        self.player.render(screen, camera_pos)

        self.stage.get_info().render(screen)

        if self.is_clear or self.is_game_over:
            self.ranking_frame.render(screen)

        if self.is_pause:
            self._render_pause(screen)

        if not self.start_counter.is_finished():
            self.start_counter.render(screen)

    def _render_background(self, screen):
        background = self.stage.get_background()
        bw, bh = background.get_rect().size
        sw, sh = self.scene.get_bound()
        cy = sh + (bh - sh) * (self.camera.pos() / 50000)

        x, y = 0, max(0, bh - cy)

        screen.blit(background, (0, 0), (1000, y, sw, sh))

    def _render_pause(self, screen):
        (x, y) = self.get_scene().get_bound()

        show_text(screen, "PAUSE", WHITE, 50, (x/2, y/2), align_hor="center", align_ver="center")

    def _check_player(self, delta):
        if self.player.get_position().y < self.camera.pos():
            self.game_over()
            return

        self._check_platforms(delta)
        self._check_items(delta)
        self._check_monsters(delta)

    def _check_platforms(self, delta):
        for p in self.stage.get_platforms():
            if not p.is_touchable:
                continue

            if self.player.is_dropping():
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

    def _check_monsters(self, delta):
        for m in self.stage.get_monsters():
            if not m.is_touchable:
                continue

            if self.player.is_on(m):
                if self.player.is_dropping() and m.is_align_bottom_with(self.player):
                    m.on_steped(self.player)
            elif self.player.is_touch(m):
                m.on_touched(self.player)

            self._check_bullets(delta, m)

    def _check_bullets(self, delta, monster):
        for b in self.bullets:
            if not b.is_alive:
                continue

            if b.is_touch(monster):
                monster.die()
                b.destroy()
                return

    def _check_mission(self):
        if self.stage.check_mission(self.counter):
            self.is_clear = True
            self._show_ranking()

    def _show_ranking(self):
        ranking_data = self.db.get_records(self.stage.get_id())

        self.ranking_frame.update_ranking(ranking_data)
        self.ranking_frame.show()
        print('show')
        if self.is_game_over:
            return

        if len(ranking_data) < 10 or self.counter.get_time() < ranking_data[9][2]:
            self.ranking_frame.add_record(self.stage.get_id(), self.counter.get_time())


class StartCounter(Entity):
    def __init__(self, env):
        self.env = env
        self.progress = 0.0

        self._init_cover()

    def _init_cover(self):
        self.cover = pygame.Surface(self.env.scene.get_bound())
        self.cover.set_alpha(150)
        self.cover.fill(BLACK)

    def is_finished(self):
        return self.progress >= 3.0

    def update(self, delta):
        self.progress += delta

    def render(self, surface):
        surface.blit(self.cover, (0, 0))
        self._render_mission_message(surface)
        self._render_count(surface)

    def _render_mission_message(self, surface):
        msg = self.env.stage.get_mission_message()
        x = self.env.scene.get_bound()[0] / 2
        y = 200

        show_text(surface, msg, WHITE, 50, (x, y), align_hor="center")

    def _render_count(self, surface):
        bw, bh = self.env.scene.get_bound()

        pygame.draw.rect(surface, BLACK, (0, bh/2 - 75, bw, 150))

        number = 3 - int(self.progress)
        state = self.progress % 1.0
        font_size = int(max(80, 280 - 200 * state / 0.3))

        show_text(surface,
                  str(number),
                  WHITE,
                  font_size,
                  (int(bw/2), int(bh/2)),
                  align_hor="center",
                  align_ver="center")
