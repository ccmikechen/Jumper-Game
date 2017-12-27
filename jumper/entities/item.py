import pygame
from jumper.env_entity import EnvEntity

class Item(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(30, 30)

    def update(self, delta):
        pass

    def render(self, surface, camera):
        if not self.is_visible:
            return

        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        pygame.draw.rect(surface, self.get_color(), (x, y + camera, w, h))

    def get_color(self):
        return (0, 0, 0)

    def get_name(self):
        return 'item'

    def active(self, player):
        player.add_item(self)
        self.is_touchable = False
        self.is_visible = False

    def reactive(self, player):
        pass

    def destory(self, player):
        super().destroy()

        player.remove_item(self)

    def on_jump(self, player):
        pass

    def on_drop(self, player):
        pass

    def on_attack(self, player):
        pass
