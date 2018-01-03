import pygame
from jumper.entity import Entity
from jumper.game_helper import show_text
from jumper.entities.ui.text_input import TextInput
from jumper.timer import parse_time
from jumper.resource import R

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class NameInputFrame(Entity):
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.is_new_record = False
        self.surface = pygame.Surface(self.size)

        self.background = pygame.transform.scale(R.get_image("black_board"), self.size)

        self.reset()

    def reset(self):
        self._init_name_input()

    def _init_name_input(self):
        w, h = 300, 80
        x, y = (self.size[0] - w) / 2, 350
        self.name_input = TextInput(BLACK,
                                    40,
                                    (w, h),
                                    (x, y))
        self.name_input.on_submit(self.submit)

    def set_time(self, time):
        self.time = time

    def on_submit(self, func):
        self.on_submit_func = func

    def submit(self, name):
        self.on_submit_func(name)

    def key_down(self, key):
        self.name_input.key_down(key)

    def key_up(self, key):
        self.name_input.key_up(key)

    def set_is_new_record(self, b):
        self.is_new_record = b

    def update(self, delta):
        self.name_input.update(delta)

    def render(self, parent_surface):
        self.surface.blit(self.background, (0, 0))

        self._render_title()
        self.name_input.render(self.surface)

        parent_surface.blit(self.surface, self.position)

    def _render_title(self):
        x = self.size[0]/2

        if self.is_new_record:
            show_text(self.surface,
                      "New record!",
                      YELLOW,
                      50,
                      (x, 60),
                      align_hor="center")
        else:
            show_text(self.surface,
                      "Mission clear!",
                      WHITE,
                      50,
                      (x, 60),
                      align_hor="center")

        show_text(self.surface,
                  "Spent time:",
                  WHITE,
                  40,
                  (x, 130),
                  align_hor="center")

        show_text(self.surface,
                  parse_time(self.time),
                  WHITE,
                  40,
                  (x, 180),
                  align_hor="center")

        show_text(self.surface,
                  "Your name?",
                  WHITE,
                  40,
                  (self.size[0]/2, 280),
                  align_hor="center")
