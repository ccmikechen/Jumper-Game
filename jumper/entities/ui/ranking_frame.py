import pygame
from jumper.entity import Entity
from jumper.game_helper import show_text
from jumper.entities.ui.name_input_frame import NameInputFrame
from jumper.timer import parse_time
from jumper.db.database import Database
from jumper.resource import R
from math import copysign

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
SELECTED_GREEN = (0, 150, 0)
GREEN = (0, 255, 0)
TITLE_GRAY = (50, 50, 50)
DATA_GRAY = (80, 80, 80)
GRAY = (100, 100, 100)

class RankingFrame(Entity):
    def __init__(self, scene, position=(0, 0)):
        self.scene = scene
        self.size = (600, 900)
        self.position = position
        self.is_hidden = True
        self.surface = pygame.Surface(self.size)
        self.ranking_list = RankingList((550, 600), (25, 150))
        self.option_selector = OptionSelector((self.size[0], 50),
                                              (0, 750))
        self.db = Database()

        self.background = R.get_image("ranking_bg")

        self.reset()

    def reset(self):
        self.is_show_name_input = False
        self._init_name_input()
        self._new_record_stage = None
        self._new_record_time = None
        self.option_selector.reset()
        self._init_cover()

    def _init_name_input(self):
        w, h = 500, 500
        x, y = (self.size[0] - w) / 2, (self.size[1] - h) / 2
        self.name_input = NameInputFrame((w, h), (x, y))
        self.name_input.on_submit(self.on_name_submit)

    def _init_cover(self):
        self.cover = pygame.Surface(self.size)
        self.cover.set_alpha(200)
        self.cover.fill(BLACK)

    def update_ranking(self, ranking_data):
        self.ranking_list.update_ranking(ranking_data)

    def show(self):
        self.is_hidden = False

    def hide(self):
        self.is_hidden = True

    def add_record(self, stage, time):
        self._new_record_stage = stage
        self._new_record_time = time
        self.name_input.set_time(time)
        self.is_show_name_input = True

    def on_name_submit(self, name):
        self.db.add_record(self._new_record_stage, self._new_record_time, name)
        self.is_show_name_input = False
        self.update_ranking(self.db.get_records(self._new_record_stage))

    def disable_next_stage_option(self):
        self.option_selector.set_option("Next", False)

    def key_down(self, key):
        if self.is_hidden: return

        if self.is_show_name_input:
            self.name_input.key_down(key)
            return

        if key == pygame.K_RIGHT:
            self.option_selector.next()
        if key == pygame.K_LEFT:
            self.option_selector.prev()
        if key == pygame.K_RETURN:
            self._execute_option()

    def key_up(self, key):
        if self.is_hidden: return

        if self.is_show_name_input:
            self.name_input.key_up(key)

    def update(self, delta):
        if self.is_show_name_input:
            self.name_input.update(delta)

    def render(self, parent_surface):
        if self.is_hidden: return

        self.surface.blit(self.background, (0, 0))
        self._render_title()
        self.ranking_list.render(self.surface)
        self.option_selector.render(self.surface)

        if self.is_show_name_input:
            self.surface.blit(self.cover, (0, 0))
            self.name_input.render(self.surface)

        parent_surface.blit(self.surface, self.position)

    def _render_title(self):
        x = self.size[0] / 2
        y = 70

        show_text(self.surface, "RANKING", TITLE_GRAY, 50, (x, y), align_hor="center")

    def _execute_option(self):
        option = self.option_selector.get_selected()

        if option["name"] == "Home":
            self.scene.start_and_reset_scene("home")
        elif option["name"] == "Again":
            stage_id = self.scene.environment.get_stage().get_id()
            self.scene.reset(params={"stage": stage_id})
        elif option["name"] == "Next":
            next_stage_id = self.scene.environment.get_next_stage_id()
            self.scene.reset(params={"stage": next_stage_id})

class RankingList(Entity):
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.ranking_data = []

    def update_ranking(self, ranking_data):
        self.ranking_data = ranking_data

    def render(self, surface):
#        self._render_border(surface)
        self._render_data(surface)

    def _render_border(self, surface):
        x, y = self.position
        w, h = self.size

        pygame.draw.rect(surface, GREEN, (x, y, w, h), 10)

    def _render_data(self, surface):
        for i in range(0, min(10, len(self.ranking_data))):
            (_, _, time, name) = self.ranking_data[i]
            x = self.position[0]
            y = self.position[1] + 30 + 50 * i

            show_text(surface, str(i + 1), DATA_GRAY, 30, (x + 30, y))
            show_text(surface, name, DATA_GRAY, 30, (x + 80, y))
            show_text(surface, parse_time(time), DATA_GRAY, 30, (x + 400, y))

class OptionSelector(Entity):
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.selected = 0

        self.reset()

    def reset(self):
        self.options = {
            0: {"name": "Again", "enable": True},
            1: {"name": "Home", "enable": True},
            2: {"name": "Next", "enable": True}
        }

    def set_option(self, name, enable):
        for i in self.options:
            if self.options[i]["name"] == name:
                self.options[i]["enable"] = enable

    def move_cursor(self, n):
        self.selected = (self.selected + n) % len(self.options)

        if self.options[self.selected]["enable"] == False:
            self.move_cursor(copysign(1, n))

    def next(self):
        self.move_cursor(1)

    def prev(self):
        self.move_cursor(-1)

    def get_selected(self):
        return self.options[self.selected]

    def render(self, surface):
        for i in self.options:
            option = self.options[i]
            color = GRAY
            if i == self.selected:
                color = SELECTED_GREEN
            if option["enable"] == False:
                color = WHITE

            x = self.position[0] + (self.size[0] / (len(self.options) + 1)) * (i + 1)
            y = self.position[1] + (self.size[1] / 2)

            show_text(surface,
                      option["name"],
                      color,
                      40,
                      (x, y),
                      align_hor="center",
                      align_ver="center")
