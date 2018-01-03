from jumper.pattern import Pattern
from jumper.entities.platforms.normal_platform import NormalPlatform
from jumper.config import config
from random import randint

class PatternA1(Pattern):
    """
    Stage 1 normal platforms
    """
    def __init__(self, env, level):
        super().__init__(env, level)
        (width, height) = env.get_scene().get_bound()

        self.levels = 30

        platforms = []
        for i in range(0, 10):
            (x, y) = self.get_random_position(level + i * 3)

            platforms.append(NormalPlatform(env, (x, y)))

        self.platforms = platforms
