class Entity:
    def update(self, _delta, _params={}):
        raise NotImplementedError()

    def render(self, _surface, _camera=None):
        raise NotImplementedError()
