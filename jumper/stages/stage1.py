from jumper.stage import Stage
from jumper.patterns.pattern_a_0 import PatternA0
from jumper.patterns.pattern_a_1 import PatternA1
from jumper.patterns.pattern_a_2 import PatternA2
from jumper.patterns.pattern_a_3 import PatternA3
from jumper.entities.stage_info import StageInfo

class Stage1(Stage):
    class PatternGen:
        def __init__(self, env):
            self.env = env

        def generate(self, level):
            if level == 0:
                return PatternA0(self.env, level)
            # elif level < 100:
            #     return PatternA1(self.env, level)
            # elif level < 200:
            #     return PatternA2(self.env, level)
            else:
            #     return PatternA3(self.env, level)
                return PatternA2(self.env, level)
    def __init__(self, environment):
        super().__init__(environment)
        self.pattern_gen = Stage1.PatternGen(environment)
        self.last_level = 0
        self.info = StageInfo()
        self.background = (100, 100, 100)

    def update(self, level):
        if level > self.last_level - 30:
            pattern = self.pattern_gen.generate(self.last_level)
            self.add_pattern(pattern)
            self.last_level += pattern.get_levels()

