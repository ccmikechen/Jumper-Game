import pygame
from jumper.entity import Entity
from jumper.game_helper import show_text
from jumper.resource import R

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Information(Entity):
    def __init__(self):
        self.title = R.get_image("title")
        self.bliping_progress = 0.0

    def update(self, delta):
        self.bliping_progress = (self.bliping_progress + delta) % 1.0

    def render(self, screen):
        bound = screen.get_size()

        _, th = self.title.get_rect().size
        tw = int(420 * 1.5)
        screen.blit(self.title, ((bound[0] - tw)/2, 100), (0, 0, tw, th))

        if self.bliping_progress < 0.5:
            show_text(screen, 'press SPACE to start', WHITE, 40, (bound[0]/2, 500), align_hor="center")

        show_text(screen, 'Made by', WHITE, 20, (bound[0] - 300, bound[1] - 100))
        show_text(screen, '四資四甲 1103137124 陳銘嘉', WHITE, 20, (bound[0] - 300, bound[1] - 50))
