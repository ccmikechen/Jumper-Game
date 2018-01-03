from jumper.stage import Stage
from jumper.patterns.pattern_e_0 import PatternE0
from jumper.patterns.pattern_e_1 import PatternE1
from jumper.patterns.pattern_e_2 import PatternE2
from jumper.patterns.pattern_e_3 import PatternE3
from jumper.resource import R
from jumper.config import config

class Stage5(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level < 50:
                return PatternE0(self.env, level)
            elif level < 150:
                return PatternE1(self.env, level)
            elif level < 300:
                return PatternE2(self.env, level)
            else:
                return PatternE3(self.env, level)

    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage5.PatternGen(environment)

        self.background = R.get_image("stage5_bg")
        self.music = "stage5"
        self.id = 5
        config.G = 999999

    def check_mission(self, counter):
        return counter.get_total_monsters()["die"] >= 100

    def get_mission_message(self):
        return ["Kill 100 monsters"]

    def get_next_stage_id(self):
        return None
