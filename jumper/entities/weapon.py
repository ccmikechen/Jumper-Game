from jumper.entities.item import Item

class Weapon(Item):
    def trigger(self, env):
        pass

    def get_type(self):
        return 'weapon'
