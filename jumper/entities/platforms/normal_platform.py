from jumper.entities.platform import Platform

class NormalPlatform(Platform):
    def get_color(self):
        return (0, 128, 255)

    def active(self):
        self.environment.player.jump(v=1500)
