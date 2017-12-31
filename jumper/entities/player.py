import pygame
from jumper.config import config
from jumper.env_entity import EnvEntity
from jumper.entities.weapons.bb_gun import BBGun
from jumper.resource import R

LEFT, RIGHT = 0, 1

class Player(EnvEntity):
    def __init__(self, environment, position):
        super().__init__(environment, position)
        self.set_size(70, 70)
        self.v = 0
        self.is_moving_left = False
        self.is_moving_right = False
        self.direction = RIGHT
        self.items = []
        self.animation = NinjaAnimetion(self.size.int())

        default_weapon = BBGun(environment, (0, 0))
        default_weapon.active(self)
        self.weapon = default_weapon

    def jump(self, v=1500):
        self.v = v

        for item in self.items:
            item.on_jump(self)

    def die(self):
        pass

    def attack(self):
        if self.weapon != None:
            self.weapon.trigger(self.environment, self)
            self.animation.update_is_attacking()

    def start_moving_left(self):
        self.is_moving_left = True
        self.direction = LEFT
        self.animation.update_direction(LEFT)

    def start_moving_right(self):
        self.is_moving_right = True
        self.direction = RIGHT
        self.animation.update_direction(RIGHT)

    def stop_moving_left(self):
        self.is_moving_left = False

    def stop_moving_right(self):
        self.is_moving_right = False

    def get_v(self):
        return self.v

    def get_direction(self):
        return self.direction

    def is_dropping(self):
        return self.v < 0

    def pos(self):
        return self.position

    def add_item(self, new_item):
        if new_item.get_type() == 'weapon':
            self.weapon = new_item
            return

        for item in self.items:
            if item.get_name() == new_item.get_name():
                item.reactive(self)
                return

        new_item.reactive(self)
        self.items.append(new_item)

    def remove_item(self, item):
        for i in range(0, len(self.items)):
            if self.items[i].get_name() == item.get_name():
                del self.items[i]
                return
        print(self.items)

    def update(self, delta):
        s = 1 / (2 * config.G * delta)
        self.v -= s
        self.position.y += self.v * delta

        (env_width, env_height) = self.environment.get_scene().get_bound()

        if self.is_moving_left:
            self.position.x -= delta * 1000
            if self.right() <= 0:
                self.position.x += env_width
        if self.is_moving_right:
            self.position.x += delta * 1000
            if self.left() >= env_width:
                self.position.x -= env_width

        self.animation.update(delta, self.v)

    def render(self, surface, camera):
        (x, y) = self.get_view_position().int()

        self.animation.render(surface, (x, y + camera - 20))

class NinjaAnimetion:
    def __init__(self, size):
        self.size = size
        self.direction = RIGHT
        self.is_jumping = False
        self.is_attacking = False
        self.jumping_progress = 0
        self.falling_progress = 0
        self.attacking_progress = 0
        self.images = {}

        self._init_images(R.get_sprite_sheet("ninja"))

    def _init_images(self, sprite_sheet):
        self.images["jumping_1"] = pygame.transform.scale(sprite_sheet.image_at(0, 9), self.size)
        self.images["jumping_2"] = pygame.transform.scale(sprite_sheet.image_at(1, 9), self.size)
        self.images["jumping_3"] = pygame.transform.scale(sprite_sheet.image_at(2, 9), self.size)
        self.images["jumping_4"] = pygame.transform.scale(sprite_sheet.image_at(3, 9), self.size)
        self.images["jumping_5"] = pygame.transform.scale(sprite_sheet.image_at(4, 9), self.size)
        self.images["jumping_6"] = pygame.transform.scale(sprite_sheet.image_at(5, 9), self.size)
        self.images["jumping_7"] = pygame.transform.scale(sprite_sheet.image_at(6, 9), self.size)
        self.images["falling_1"] = pygame.transform.scale(sprite_sheet.image_at(7, 9), self.size)
        self.images["falling_2"] = pygame.transform.scale(sprite_sheet.image_at(8, 9), self.size)
        self.images["falling_3"] = pygame.transform.scale(sprite_sheet.image_at(9, 9), self.size)
        self.images["falling_4"] = pygame.transform.scale(sprite_sheet.image_at(10, 9), self.size)
        self.images["falling_5"] = pygame.transform.scale(sprite_sheet.image_at(11, 9), self.size)
        self.images["attacking_1"] = pygame.transform.scale(sprite_sheet.image_at(8, 3), self.size)
        self.images["attacking_2"] = pygame.transform.scale(sprite_sheet.image_at(9, 3), self.size)
        self.images["attacking_3"] = pygame.transform.scale(sprite_sheet.image_at(10, 3), self.size)

    def is_align_left_with(self, entity):
        return self.left() - 15 <= entity.right() and self.left() >= entity.left()

    def is_align_right_with(self, entity):
        return self.right() + 15 >= entity.left() and self.right() <= entity.right()

    def update_is_attacking(self):
        self.is_attacking = True

    def update_direction(self, direction):
        self.direction = direction

    def update(self, delta, v):
        if self.is_attacking:
            self.attacking_progress += delta

            if self.attacking_progress >= 0.12:
                self.is_attacking = False
                self.attacking_progress = 0.0

        elif self.is_jumping:
            self.jumping_progress += delta

            if v < 0:
                self.is_jumping = False
                self.jumping_progress = 0.0

        else:
            self.falling_progress += delta

            if v > 0:
                self.is_jumping = True
                self.falling_progress = 0.0

    def render(self, surface, position):
        image = None

        if self.is_attacking:
            if self.attacking_progress < 0.04:
                image = self.images["attacking_1"]
            elif self.attacking_progress < 0.8:
                image = self.images["attacking_2"]
            else:
                image = self.images["attacking_3"]
        elif self.is_jumping:
            if self.jumping_progress < 0.04:
                image = self.images["jumping_1"]
            elif self.jumping_progress < 0.08:
                image = self.images["jumping_2"]
            elif self.jumping_progress < 0.12:
                image = self.images["jumping_3"]
            elif self.jumping_progress < 0.16:
                image = self.images["jumping_4"]
            elif self.jumping_progress < 0.20:
                image = self.images["jumping_5"]
            elif self.jumping_progress < 0.24:
                image = self.images["jumping_6"]
            else:
                image = self.images["jumping_7"]
        else:
            if self.falling_progress < 0.04:
                image = self.images["falling_1"]
            elif self.falling_progress < 0.08:
                image = self.images["falling_2"]
            elif self.falling_progress < 0.12:
                image = self.images["falling_3"]
            elif self.falling_progress < 0.16:
                image = self.images["falling_4"]
            else:
                image = self.images["falling_5"]

        if self.direction == LEFT:
            image = pygame.transform.flip(image, True, False)

        surface.blit(image, position)
