from jumper.entities.platforms.normal_platform import NormalPlatform

class Stage:
    def __init__(self, environment):
        self.environment = environment
        self.background = (0, 0, 0)
        self.reset()

    def reset(self):
        self.platforms = []
        self.items = []
        self.objects = []
        self.monsters = []

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

    def check_mission(self):
        pass

    def update(self):
        pass
