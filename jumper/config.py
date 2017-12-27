class Config:
    def __init__(self):
        self.reset()

    def reset(self):
        self.reset_G()
        self.reset_MAX_SPEED()
        self.reset_LEVEL_HEIGHT()

    def reset_G(self):
        self.G = 1.5

    def reset_MAX_SPEED(self):
        self.MAX_SPEED = 1000

    def reset_LEVEL_HEIGHT(self):
        self.LEVEL_HEIGHT = 30

config = Config()
