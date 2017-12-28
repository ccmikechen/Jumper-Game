from jumper.entities.weapon import Weapon
from jumper.entities.bullets.bb_bullet import BBBullet

class BBGun(Weapon):
    def trigger(self, env, player):
        x = player.get_position().x + 10
        y = player.get_position().y + 30

        env.add_bullet(BBBullet(env, (x, y), 90))

