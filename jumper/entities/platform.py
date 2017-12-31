import pygame
from jumper.env_entity import EnvEntity

class Platform(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(100, 30)
        self.image = None

    def update(self, delta):
        pass

    def render(self, surface, camera):
        if not self.is_alive:
            return

        (x, y) = self.get_view_position().int()
        (w, h) = self.get_size().int()

        if self.get_image() == None:
            pygame.draw.rect(surface, self.get_color(), (x, y + camera, w, h))
        else:
            surface.blit(self.image, (x, y + camera))

    def get_color(self):
        return (0, 0, 255)

    def get_image(self):
        return self.image

    def active(self):
        pass
