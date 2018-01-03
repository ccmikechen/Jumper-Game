from random import randint
from jumper.config import config

class Pattern:
    def __init__(self, env, level):
        self.env = env
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

    def get_random_position(self, level):
        (width, height) = self.env.get_scene().get_bound()

        x = randint(0, int((width - 100) / 50) * 50)
        y = config.LEVEL_HEIGHT * level

        return (x, y)
