from jumper.stage import Stage
from jumper.patterns.pattern_a_0 import PatternA0
from jumper.patterns.pattern_c_0 import PatternC0
from jumper.patterns.pattern_c_1 import PatternC1
from jumper.patterns.pattern_c_2 import PatternC2
from jumper.patterns.pattern_c_3 import PatternC3
from jumper.resource import R

class Stage3(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level == 0:
                return PatternA0(self.env, level)
            elif level < 50:
                return PatternC0(self.env, level)
            elif level < 200:
                return PatternC1(self.env, level)
            elif level < 400:
                return PatternC2(self.env, level)
            else:
                return PatternC3(self.env, level)

    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage3.PatternGen(environment)

        self.background = R.get_image("stage3_bg")
        self.id = 3

    def check_mission(self, counter):
        return counter.get_monster("Slime")["die"] >= 10

    def get_mission_message(self):
        return ["Kill 10 slimes"]
