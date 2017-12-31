import pygame
from jumper.entities.weapon import Weapon
from jumper.entities.bullets.bb_wave_bullet import BBWaveBullet
from jumper.resource import R

class BBWavegun(Weapon):
    def __init__(self, environment, position):
        super().__init__(environment, position, 'BB Wavegun')
        self.image = pygame.transform.scale(R.get_image("bb_wavegun"), self.size.int())

    def trigger(self, env, player):
        x = player.get_position().x
        x = x if player.direction == 0 else x + 60
        y = player.get_position().y + 30

        env.add_bullet(BBWaveBullet(env, (x, y), 90, speed=2000))

    def get_color(self):
        return (100, 255, 100)
