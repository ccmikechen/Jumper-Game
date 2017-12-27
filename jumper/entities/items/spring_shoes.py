from jumper.entities.item import Item

class SpringShoes(Item):
    def get_color(self):
        return (0, 255, 0)

    def get_name(self):
        return 'Sprint shoes'

    def render(self, surface, camera):
        super().render(surface, camera)

    def active(self, player):
        super().active(player)

    def reactive(self, player):
        self.count = 6

    def on_jump(self, player):
        player.v = 2500
        self.count -= 1

        if self.count <= 0:
            self.destory(player)
