from jumper.entities.weapon import Weapon
from jumper.entities.bullets.bb_bullet import BBBullet

class BBShotgun(Weapon):
    def trigger(self, env, player):
        x = player.get_position().x + 10
        y = player.get_position().y + 30

        env.add_bullet(BBBullet(env, (x, y), 90))
        env.add_bullet(BBBullet(env, (x, y), 70))
        env.add_bullet(BBBullet(env, (x, y), 110))

    def get_color(self):
        return (0, 255, 255)
