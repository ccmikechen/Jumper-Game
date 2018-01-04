from jumper.stage import Stage
from jumper.patterns.pattern_a_0 import PatternA0
from jumper.patterns.pattern_b_1 import PatternB1
from jumper.patterns.pattern_b_2 import PatternB2
from jumper.patterns.pattern_b_3 import PatternB3
from jumper.patterns.pattern_b_4 import PatternB4
from jumper.resource import R

class Stage2(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level == 0:
                return PatternA0(self.env, level)
            elif level < 300:
                return PatternB1(self.env, level)
            elif level < 600:
                return PatternB2(self.env, level)
            elif level < 1000:
                return PatternB3(self.env, level)
            else:
                return PatternB4(self.env, level)

    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage2.PatternGen(environment)

        self.background = R.get_image("stage2_bg")
        self.music = "stage2"
        self.id = 2

    def check_mission(self, counter):
        return counter.get_item("Coin")["active"] >= 5

    def get_mission_message(self):
        return ["Find 5 coins"]
