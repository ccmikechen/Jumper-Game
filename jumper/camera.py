class Camera:
    def __init__(self, speed = 1.0, position = 0.0):
        self.set_pos(position)
        self.set_speed(speed)

    def move(self, dist):
        self.dist_position = dist

    def set_pos(self, position):
        self.position = float(position)
        self.dist_position = float(position)

    def pos(self):
        return self.position

    def set_speed(self, speed):
        self.speed = float(speed)

    def update(self, delta):
        d = self.dist_position - self.position

        if abs(d) >= 1.0:
            self.position += d * (delta / self.speed)
        else:
            self.position = self.dist_position

