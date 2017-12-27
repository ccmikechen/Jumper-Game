from jumper.entities.platform import Platform

class WeakPlatform(Platform):
    def get_color(self):
        return (0, 128, 128)

    def active(self):
        if self.is_touchable and self.is_alive:
            self.destroy()
