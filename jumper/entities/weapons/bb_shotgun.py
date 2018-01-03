import pygame
from jumper.entities.weapon import Weapon
from jumper.entities.bullets.bb_bullet import BBBullet
from jumper.resource import R

class BBShotgun(Weapon):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'BB Shotgun')
        self.image = pygame.transform.scale(R.get_image("bb_shotgun"), self.size.int())

    def trigger(self, env, player):
        x = player.get_position().x
        x = x if player.direction == 0 else x + 60
        y = player.get_position().y + 30

        env.add_bullet(BBBullet(env, (x, y), 90))
        env.add_bullet(BBBullet(env, (x, y), 70))
        env.add_bullet(BBBullet(env, (x, y), 110))
        R.play_sound("shotgun")

    def get_color(self):
        return (0, 255, 255)
