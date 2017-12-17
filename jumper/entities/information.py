from jumper.entity import Entity
from jumper.game_helper import show_text

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Information(Entity):
    def update(self, delta):
        pass

    def render(self, screen):
        bound = screen.get_size()
        show_text(screen, 'Snake Battle', WHITE, 100, (250, 150))
        show_text(screen, 'press SPACE to start', WHITE, 40, (250, 350))
        show_text(screen, 'Player 1 - A = turn left, D = turn right', WHITE, 30, (250, 450))
        show_text(screen, 'Player 2 - J = turn left, L = turn right', WHITE, 30, (250, 550))

        show_text(screen, 'Made by', WHITE, 20, (bound[0] - 400, bound[1] - 400))
        show_text(screen, '四資四甲 1103137124 陳銘嘉', WHITE, 20, (bound[0] - 400, bound[1] - 350))
        show_text(screen, '四子四乙 1103105242 陳冠宏', WHITE, 20, (bound[0] - 400, bound[1] - 300))
        show_text(screen, '四工二甲 1105107148 周晉毅', WHITE, 20, (bound[0] - 400, bound[1] - 250))
