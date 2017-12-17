from jumper.stage import Stage
from jumper.entities.platforms.normal_platform import NormalPlatform

class Stage1(Stage):
    def __init__(self, environment):
        super().__init__(environment)

        self.background = (100, 100, 100)

        init_platforms = [
            NormalPlatform(self.environment, (200, 30)),
            NormalPlatform(self.environment, (300, 90)),
            NormalPlatform(self.environment, (100, 210)),
            NormalPlatform(self.environment, (400, 480))
        ]
        self.platforms.extend(init_platforms)
