from jumper.entity import Entity

class EnvEntity(Entity):
    def __init__(self, environment, position):
        self.environment = environment
        (x, y) = position
        self.position = Position(x, y)
        self.size = Size(.0, .0)

    def get_view_position(self):
        (_, height) = self.environment.get_scene().get_bound()
        new_y = self.position.y - self.environment.get_level()
        new_y = height - new_y

        return Position(self.position.x, new_y)

    def set_position(self, x, y):
        self.position = Position(x, y)

    def get_position(self):
        return self.position

    def set_size(self, w, h):
        self.size = Size(w, h)

    def get_size(self):
        return self.size

    def top(self):
        return self.position.x + self.size.h

    def bottom(self):
        return self.position.x

    def left(self):
        return self.position.y

    def right(self):
        return self.position.y + self.size.w

class Position:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def int(self):
        return (int(self.x), int(self.y))

class Size:
    def __init__(self, w, h):
        self.w = float(w)
        self.h = float(h)

    def int(self):
        return (int(self.w), int(self.h))
