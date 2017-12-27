from jumper.pattern import Pattern
from jumper.entities.platforms.normal_platform import NormalPlatform
from random import randint

class PatternA0(Pattern):
    """
    Stage 1 initial platform
    """
    def __init__(self, env, level):
        super().__init__(env, level)
        (width, height) = env.get_scene().get_bound()

        self.levels = 6

        platforms = []
        for i in range(0, int(width / 100)):
            x = i * 100
            y = 0
            platforms.append(NormalPlatform(env, (x, y)))

        self.platforms = platforms
