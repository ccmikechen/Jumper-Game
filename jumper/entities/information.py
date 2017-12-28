from jumper.entity import Entity
from jumper.game_helper import show_text

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Information(Entity):
    def update(self, delta):
        pass

    def render(self, screen):
        bound = screen.get_size()
        show_text(screen, 'Maple Jump', WHITE, 80, (bound[0]/2, 100), align_hor="center")
        show_text(screen, 'press SPACE to start', WHITE, 40, (bound[0]/2, 500), align_hor="center")

        show_text(screen, 'Made by', WHITE, 20, (bound[0] - 300, bound[1] - 100))
        show_text(screen, '四資四甲 1103137124 陳銘嘉', WHITE, 20, (bound[0] - 300, bound[1] - 50))
