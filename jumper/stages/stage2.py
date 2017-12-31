from jumper.stage import Stage
from jumper.patterns.pattern_a_0 import PatternA0
from jumper.patterns.pattern_a_1 import PatternA1
from jumper.patterns.pattern_a_2 import PatternA2
from jumper.patterns.pattern_a_3 import PatternA3
from jumper.entities.stage_info import StageInfo
from jumper.resource import R

class Stage2(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level == 0:
                return PatternA0(self.env, level)
            else:
                return PatternA3(self.env, level)

    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage2.PatternGen(environment)
        self.last_level = 0
        self.background = R.get_image("stage2_bg")
        self.id = 2

    def update(self, level):
        super().update()

        if level > self.last_level - 30:
            pattern = self.pattern_gen.generate(self.last_level)
            self.add_pattern(pattern)
            self.last_level += pattern.get_levels()

    def check_mission(self, counter):
        return counter.get_total_monsters()["die"] >= 20

    def get_mission_message(self):
        return "Find 10 dimands"
