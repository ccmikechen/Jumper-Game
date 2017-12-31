from functools import reduce

class GameCounter:
    def __init__(self):
        self.reset()

    def reset(self):
        self.level = 0
        self.time = 0
        self.steps = 0
        self.items = {}
        self.monsters = {}
        self.weapons = {}
        self.attacks = 0

    def update_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def update_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def inc_step(self):
        self.steps += 1

    def get_steps(self):
        return self.steps

    def inc_item_appear(self, name):
        self._init_item(name)
        self.items[name]["appear"] += 1

    def inc_item_active(self, name):
        self._init_item(name)
        self.items[name]["active"] += 1

    def get_item(self, name):
        self._init_item(name)
        return self.items[name]

    def get_total_items(self):
        return reduce(lambda acc, i: self._default_item(
            appear = acc["appear"] + self.items[i]["appear"],
            active = acc["active"] + self.items[i]["active"]
        ), self.items, self._default_item())

    def _init_item(self, name):
        if not name in self.items:
            self.items[name] = self._default_item()

    def _default_item(self, appear=0, active=0):
        return {
            "appear": appear,
            "active": active
        }

    def inc_monster_appear(self, name):
        self._init_monster(name)
        self.monsters[name]["appear"] += 1

    def inc_monster_die(self, name):
        self._init_monster(name)
        self.monsters[name]["die"] += 1

    def get_monster(self, name):
        self._init_monster(name)
        return self.monsters[name]

    def get_total_monsters(self):
        return reduce(lambda acc, i: self._default_monster(
            appear = acc["appear"] + self.monsters[i]["appear"],
            die = acc["die"] + self.monsters[i]["die"]
        ), self.monsters, self._default_monster())

    def _init_monster(self, name):
        if not name in self.monsters:
            self.monsters[name] = self._default_monster()

    def _default_monster(self, appear=0, die=0):
        return {
            "appear": appear,
            "die": die
        }

    def inc_attack(self):
        self.attacks += 1

    def get_attacks(self):
        return self.attacks
