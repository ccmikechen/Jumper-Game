import pygame
from jumper.entity import Entity
from jumper.game_helper import show_text
from jumper.resource import R

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (48, 48, 48)
YELLOW = (180, 180, 0)

class StageSelector(Entity):
    def __init__(self, stages, position=(0, 0), width=400):
        self.stages = stages
        self.position = position
        self.width = width
        self.cursor = 0

        self.option_background = R.get_image("menu_option")
        self.lock_image = R.get_image("lock")

        self._init_cover()

    def _init_cover(self):
        b_size = self.option_background.get_rect().size

        self.lock_cover = pygame.Surface(b_size)
        self.lock_cover.set_alpha(200)
        self.lock_cover.fill(BLACK)

    def prev(self):
        self.cursor = (self.cursor - 1) % len(self.stages)

        if self.stages[self.cursor][1] == "locked":
            self.prev()

    def next(self):
        self.cursor = (self.cursor + 1) % len(self.stages)

        if self.stages[self.cursor][1] == "locked":
            self.next()

    def get_selected_stage(self):
        return self.stages[self.cursor][0]

    def update(self, delta):
        pass

    def render(self, surface):
        for i in range(0, len(self.stages)):
            stage = self.stages[i]
            color = YELLOW if self.cursor == i else GRAY

            text = "Stage {}".format(stage[0])

            bw, bh = self.option_background.get_rect().size
            x = self.position[0]
            y = self.position[1] + 150 * i

            surface.blit(self.option_background, (x, y))
            show_text(surface,
                      text,
                      color,
                      50,
                      (int(x + bw/2), int(y + bh/2)),
                      align_hor="center",
                      align_ver="center")

            if stage[1] == "locked":
                lw, lh = self.lock_image.get_rect().size
                lx = int(x + (bw - lw) / 2)
                ly = int(y + (bh - lh) / 2)

                surface.blit(self.lock_cover, (x, y))
                surface.blit(self.lock_image, (lx, ly))


