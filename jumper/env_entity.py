from jumper.entity import Entity

class EnvEntity(Entity):
    def __init__(self, environment, position):
        self.environment = environment
        (x, y) = position
        self.position = Position(x, y)
        self.size = Size(.0, .0)
        self.is_alive = True
        self.is_touchable = True
        self.is_visible = True

    def get_view_position(self):
        (_, height) = self.environment.get_scene().get_bound()
        new_y = height - self.position.y

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
        return self.position.y + self.size.h

    def bottom(self):
        return self.position.y

    def left(self):
        return self.position.x

    def right(self):
        return self.position.x + self.size.w

    def is_on(self, entity):
        return self.is_align_top_with(entity) and\
               (self.is_align_left_with(entity) or self.is_align_right_with(entity))

    def is_under(self, entity):
        return entity.is_on(self)

    def is_align_top_with(self, entity):
        return self.bottom() <= entity.top() and self.bottom() >= entity.bottom()

    def is_align_bottom_with(self, entity):
        return self.top() >= entity.bottom() and self.top() <= entity.top()

    def is_align_left_with(self, entity):
        return self.left() <= entity.right() and self.left() >= entity.left()

    def is_align_right_with(self, entity):
        return self.right() >= entity.left() and self.right() <= entity.right()

    def is_touch(self, entity):
        return self.right() >= entity.left() and self.left() <= entity.right() and\
               self.top() >= entity.bottom() and self.bottom() <= entity.top()

    def set_touchable(enable):
        self.is_touchable = enable

    def set_visible(enable):
        self.is_visible = enable

    def destroy(self):
        self.is_touchable = False
        self.is_visible = False
        self.is_alive = False

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
