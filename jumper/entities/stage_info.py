from jumper.entity import Entity
from jumper.game_helper import show_text
from jumper.timer import parse_time

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class StageInfo(Entity):
    def __init__(self):
        self.level = 0
        self.time = 0

    def update(self, delta, params):
        self.level = params["level"]
        self.time = params["time"]

    def render(self, screen):
        bound = screen.get_size()
        width = bound[0]
        height = bound[1]

        show_text(screen, 'LEVEL: {}'.format(self.level), WHITE, 30, (5, 5))
        show_text(screen, parse_time(self.time), WHITE, 30, (width / 2, 5), align_hor='center')
