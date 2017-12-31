import pygame

class SpriteSheet(pygame.sprite.Sprite):
    def __init__(self, image, frame_size):
        super().__init__()
        self.sprite_sheet = image
        self.frame_width = frame_size[0]
        self.frame_height = frame_size[1]

    def image_at(self, x, y):
        image = pygame.Surface([self.frame_width, self.frame_height], pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sprite_sheet,
                   (0, 0),
                   (x * self.frame_width,
                    y * self.frame_height,
                    self.frame_width,
                    self.frame_height))

        return image
