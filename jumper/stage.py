from jumper.entities.platforms.normal_platform import NormalPlatform
from jumper.entities.stage_info import StageInfo

class Stage:
    def __init__(self, environment):
        self.environment = environment
        self.info = StageInfo(environment.counter)
        self.background = (0, 0, 0)
        self.music = None

        self.reset()

    def reset(self):
        self.last_level = 0
        self.platforms = []
        self.items = []
        self.objects = []
        self.monsters = []

    def get_id(self):
        return self.id

    def get_background(self):
        return self.background

    def get_platforms(self):
        return self.platforms

    def add_platform(self, platform):
        self.platforms.append(platform)

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def get_objects(self):
        return self_objects

    def add_object(self,_object):
        self_objects.append_object

    def get_monsters(self):
        return self.monsters

    def add_monster(self, monster):
        self.monsters.append(monster)

    def add_pattern(self, pattern):
        self.platforms.extend(pattern.get_platforms())
        self.items.extend(pattern.get_items())
        self.objects.extend(pattern.get_objects())
        self.monsters.extend(pattern.get_monsters())

    def get_info(self):
        return self.info

    def get_music(self):
        return self.music

    def get_next_stage(self):
        return None

    def check_mission(self, counter):
        return False

    def get_mission_message(self):
        return ""

    def get_next_stage_id(self):
        return self.id + 1

    def update(self, level):
        camera_pos = self.environment.camera.pos()

        self.platforms = list(filter(lambda p: p.get_position().y > camera_pos, self.platforms))

        if level > self.last_level - 30:
            pattern = self.pattern_gen.generate(self.last_level)
            self.add_pattern(pattern)
            self.last_level += pattern.get_levels()
