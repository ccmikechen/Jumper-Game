from jumper.stage import Stage
from jumper.patterns.pattern_a_0 import PatternA0
from jumper.patterns.pattern_a_1 import PatternA1
from jumper.patterns.pattern_a_2 import PatternA2
from jumper.patterns.pattern_a_3 import PatternA3
from jumper.resource import R

class Stage1(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level == 0:
                return PatternA0(self.env, level)
            elif level < 200:
                return PatternA1(self.env, level)
            else:
                return PatternA2(self.env, level)

    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage1.PatternGen(environment)

        self.background = R.get_image("stage1_bg")
        self.music = "stage1"
        self.id = 1

    def check_mission(self, counter):
        return counter.get_level() >= 500

    def get_mission_message(self):
        return ["Go to 500 level"]

