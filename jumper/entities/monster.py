import pygame
from jumper.env_entity import EnvEntity

class Monster(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(70, 70)

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
        return 'monster'

    def destory(self):
        super().destroy()

    def die(self):
        self.destroy()

    def attack(self, player):
        pass

    def on_attacked(self):
        self.die()

    def on_touched(self, player):
        player.die()
        self.environment.game_over()

    def on_steped(self, player):
        self.die()
        player.jump()

