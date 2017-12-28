from jumper.entities.monster import Monster

class Slime(Monster):
    def __init__(self, environment, position):
        super().__init__(environment, position)

    def update(self, delta):
        pass

    def get_name(self):
        return 'Slime'

    def on_attacked(self):
        self.die()
