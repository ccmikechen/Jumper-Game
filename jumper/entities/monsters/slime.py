import pygame
from jumper.entities.monster import Monster
from jumper.resource import R

class Slime(Monster):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'Slime')

        self.is_damage = False
        self.damage_progress = 0.0
        self.state_progress = 0.0

        self.images = {}
        self._init_images(R.get_sprite_sheet("slime"))

    def _init_images(self, sprite_sheet):
        size = (int(self.size.w + 20), int(self.size.h + 20))

        self.images["state_1"] = pygame.transform.scale(sprite_sheet.image_at(6, 4), size).convert_alpha()
        self.images["state_2"] = pygame.transform.scale(sprite_sheet.image_at(7, 4), size).convert_alpha()
        self.images["state_3"] = pygame.transform.scale(sprite_sheet.image_at(8, 4), size).convert_alpha()

    def is_align_bottom_with(self, entity):
        return self.top() - 30 >= entity.bottom() and self.top() <= entity.top()

    def update(self, delta):
        self.state_progress = (self.state_progress + delta) % 0.8

        if self.is_damage:
            self.damage_progress += delta

            if self.damage_progress > 0.6:
                self.is_damage = False
                super().die()

    def render_monster(self, surface, position):
        image = None

        if self.state_progress < 0.2:
            image = self.images["state_1"]
        elif self.state_progress < 0.4:
            image = self.images["state_2"]
        elif self.state_progress < 0.6:
            image = self.images["state_3"]
        else:
            image = self.images["state_2"]

        if self.is_damage:
            alpha = 255 - int((self.damage_progress / 0.6) * 255)
            image = image.copy()
            image.fill((255, 0, 0, alpha), None, pygame.BLEND_RGBA_MULT)

        surface.blit(image, position)

    def die(self):
        self.is_touchable = False
        self.is_damage = True
        self.damage_progress = 0.0
        R.play_sound("slime_death")

    def on_attacked(self):
        self.die()

    def on_steped(self, player):
        super().on_steped(player)

        R.play_sound("slime_step")
