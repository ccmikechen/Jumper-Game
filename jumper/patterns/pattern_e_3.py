from jumper.pattern import Pattern
from jumper.entities.monsters.slime import Slime
from jumper.config import config
from jumper.entities.weapons.bb_gun import BBGun
from jumper.entities.weapons.bb_shotgun import BBShotgun
from jumper.entities.weapons.bb_wavegun import BBWavegun
from random import randint

class PatternE3(Pattern):
    def __init__(self, env, level):
        super().__init__(env, level)
        (width, height) = env.get_scene().get_bound()

        self.levels = 30

        last_level = -2

        for i in range(0, 10):
            state = randint(0, 15)
            (x, y) = self.get_random_position(level + i * 3)

            if i - last_level >= 5 or state < 5:
                self.generate_item(env, x, y)

                last_level = i

    def generate_item(self, env, x, y):
        p = randint(0, 40)

        if p < 3:
            self.items.append(BBShotgun(env, (x + 30, y + 50)))
        elif p < 5:
            self.items.append(BBWavegun(env, (x + 30, y + 50)))
        elif p < 40:
            self.monsters.append(Slime(env, (x + 10, y + 60)))
