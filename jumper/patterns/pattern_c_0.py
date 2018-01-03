from jumper.pattern import Pattern
from jumper.entities.platforms.weak_platform import WeakPlatform
from jumper.entities.platforms.cloud_platform import CloudPlatform
from jumper.entities.platforms.move_platform import MovePlatform
from jumper.entities.platforms.move_weak_platform import MoveWeakPlatform
from jumper.entities.platforms.move_cloud_platform import MoveCloudPlatform
from jumper.entities.platforms.heavy_platform import HeavyPlatform
from jumper.entities.items.spring_shoes import SpringShoes
from jumper.entities.items.gravity_reducer import GravityReducer
from jumper.entities.monsters.slime import Slime
from jumper.config import config
from jumper.entities.weapons.bb_gun import BBGun
from jumper.entities.weapons.bb_shotgun import BBShotgun
from jumper.entities.weapons.bb_wavegun import BBWavegun
from random import randint

class PatternC0(Pattern):
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
        p = randint(0, 150)

        if p < 2:
            self.items.append(SpringShoes(env, (x + 30, y + 50)))
        elif p < 4:
            self.items.append(GravityReducer(env, (x + 30, y + 50)))

