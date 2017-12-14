from jumper.animation import Animation
from jumper.sprite_sheet import SpriteSheet

class BloodAnimation(Animation):
    def __init__(self, time, position, size):
        super().__init__(6, time, position, size)

        self.sprite_sheet = SpriteSheet("blood", (512, 512))

    def get_frame(self, index):
        return self.sprite_sheet.image_at(index, 0)
