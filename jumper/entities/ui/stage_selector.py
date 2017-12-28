from jumper.entity import Entity
from jumper.game_helper import show_text

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

class StageSelector(Entity):
    def __init__(self, stages, position=(0, 0), width=400):
        self.stages = stages
        self.position = position
        self.width = width
        self.cursor = 0

    def prev(self):
        self.cursor = (self.cursor - 1) % len(self.stages)

        if self.stages[self.cursor][1] == "locked":
            self.prev()

    def next(self):
        self.cursor = (self.cursor + 1) % len(self.stages)

        if self.stages[self.cursor][1] == "locked":
            self.next()

    def get_selected_stage(self):
        return self.stages[self.cursor]

    def update(self, delta):
        pass

    def render(self, surface):
        for i in range(0, len(self.stages)):
            stage = self.stages[i]
            color = YELLOW if self.cursor == i else WHITE
            color = GRAY if stage[1] == "locked" else color
            text = "Stage {}".format(stage[0])
            x = self.position[0] + (self.width / 2)
            y = self.position[1] + 150 * i

            show_text(surface, text, color, 50, (x, y), align_hor="center")
