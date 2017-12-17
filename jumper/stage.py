class Stage:
    def __init__(self):
        self.background = (0, 0, 0)
        self.platforms = []
        self.items = []
        self.monsters = []

    def get_background(self):
        return self.background

    def get_platforms(self):
        return self.platforms

    def get_items(self):
        return self.items

    def get_monsters(self):
        return self.monsters

    def check_mission(self):
        pass
