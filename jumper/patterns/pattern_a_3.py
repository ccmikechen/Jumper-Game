from jumper.pattern import Pattern
from jumper.entities.platforms.normal_platform import NormalPlatform
from jumper.entities.platforms.weak_platform import WeakPlatform
from jumper.entities.monsters.slime import Slime
from jumper.config import config
from random import randint

class PatternA3(Pattern):
    """
    Stage 1 normal platforms
    """
    def __init__(self, env, level):
        super().__init__(env, level)
        (width, height) = env.get_scene().get_bound()

        self.levels = 30

        last_level = -2

        for i in range(0, 10):
            state = randint(0, 10)
            x = randint(0, int((width - 100) / 50) * 50)
            y = config.LEVEL_HEIGHT * (level + i * 3)

            if i - last_level >= 2 or state < 3:
                self.platforms.append(NormalPlatform(env, (x, y)))

                last_level = i
            elif state < 5:
                self.generate_monster(env, x, y)

    def generate_monster(self, env, x, y):
        self.monsters.append(Slime(env, (x + 10, y + 50)))
