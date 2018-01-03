from jumper.stage import Stage
from jumper.patterns.pattern_a_0 import PatternA0
from jumper.patterns.pattern_d_0 import PatternD0
from jumper.patterns.pattern_d_1 import PatternD1
from jumper.patterns.pattern_d_2 import PatternD2
from jumper.resource import R
from jumper.config import config

class Stage4(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level == 0:
                return PatternA0(self.env, level)
            elif level < 100:
                return PatternD0(self.env, level)
            elif level < 500:
                return PatternD1(self.env, level)
            else:
                return PatternD2(self.env, level)

    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage4.PatternGen(environment)

        self.background = R.get_image("stage4_bg")
        self.music = "stage4"
        self.id = 4
        config.G = 4.0

    def check_mission(self, counter):
        return counter.get_item("Coin")["active"] >= 10 and\
               counter.get_total_monsters()["die"] >= 10 and\
               counter.get_level() >= 1000

    def get_mission_message(self):
        return ["Find 10 coins", "Kill 10 monsters", "Go to level 1000"]

