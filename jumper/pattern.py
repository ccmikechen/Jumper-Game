class Pattern:
    def __init__(self, _env, level):
        self.levels = 0
        self.platforms = []
        self.items = []
        self.objects = []
        self.monsters = []

    def get_levels(self):
        return self.levels

    def get_platforms(self):
        return self.platforms

    def get_items(self):
        return self.items

    def get_objects(self):
        return self.objects

    def get_monsters(self):
        return self.monsters

