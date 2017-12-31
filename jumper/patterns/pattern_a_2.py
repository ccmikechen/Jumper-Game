from jumper.pattern import Pattern
from jumper.entities.platforms.normal_platform import NormalPlatform
from jumper.entities.platforms.weak_platform import WeakPlatform
from jumper.entities.items.spring_shoes import SpringShoes
from jumper.entities.items.gravity_reducer import GravityReducer
from jumper.config import config
from random import randint

class PatternA2(Pattern):
    """
    Stage 1 normal platforms
    """
    def __init__(self, env, level):
        super().__init__(env, level)
        (width, height) = env.get_scene().get_bound()

        self.levels = 30

        last_level = -2

        for i in range(0, 10):
            state = randint(0, 5)
            x = randint(0, int((width - 100) / 50) * 50)
            y = config.LEVEL_HEIGHT * (level + i * 3)

            if i - last_level >= 2 or state < 3:
                self.platforms.append(NormalPlatform(env, (x, y)))
                self.generate_item(env, x, y)

                last_level = i
            elif state == 3:
                self.platforms.append(WeakPlatform(env, (x, y)))

    def generate_item(self, env, x, y):
        p = randint(0, 20)

        if p == 0:
            self.items.append(SpringShoes(env, (x + 30, y + 50)))
        elif p == 1:
            self.items.append(GravityReducer(env, (x + 30, y + 50)))

