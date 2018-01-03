from jumper.pattern import Pattern
from jumper.entities.platforms.weak_platform import WeakPlatform
from jumper.entities.platforms.move_platform import MovePlatform
from jumper.entities.platforms.cloud_platform import CloudPlatform
from jumper.entities.items.spring_shoes import SpringShoes
from jumper.entities.items.gravity_reducer import GravityReducer
from jumper.entities.items.coin import Coin
from jumper.entities.monsters.slime import Slime
from jumper.config import config
from random import randint

class PatternB4(Pattern):
    def __init__(self, env, level):
        super().__init__(env, level)
        (width, height) = env.get_scene().get_bound()

        self.levels = 30

        last_level = -2

        for i in range(0, 10):
            state = randint(0, 15)
            (x, y) = self.get_random_position(level + i * 3)

            if i - last_level >= 2 or state < 3:
                self.platforms.append(CloudPlatform(env, (x, y)))
                self.generate_item(env, x, y)

                last_level = i
            elif state < 7:
                self.platforms.append(MovePlatform(env, (x, y)))
            elif state == 7:
                self.platforms.append(WeakPlatform(env, (x, y)))

    def generate_item(self, env, x, y):
        p = randint(0, 50)

        if p < 2:
            self.items.append(SpringShoes(env, (x + 30, y + 50)))
        elif p < 4:
            self.items.append(GravityReducer(env, (x + 30, y + 50)))
        elif p < 10:
            self.items.append(Coin(env, (x + 30, y + 50)))
        elif p < 15:
            self.monsters.append(Slime(env, (x + 10, y + 60)))

