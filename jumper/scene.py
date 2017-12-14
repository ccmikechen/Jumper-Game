import pygame

class Scene:
    def __init__(self, game):
        self.game = game
        self.animations = []
        self.setup()

    def setup(self):
        raise NotImplementedError()

    def update(self, delta):
        self._update_animations(delta)

    def render(self, screen):
        self._render_animations(screen)

    def start_scene(self, name):
        self.game.start_scene(name)

    def start_and_reset_scene(self, name):
        self.game.start_and_reset_scene(name)

    def play_animation(self, animation):
        animation.play()
        self.animations.append(animation)

    def on_key_down(self, _key):
        pass

    def on_key_up(self, _key):
        pass

    def get_bound(self):
        return self.game.get_bound()

    def _update_animations(self, delta):
        for animation in self.animations:
            animation.update(delta)

    def _render_animations(self, screen):
        for animation in self.animations:
            animation.render(screen)

class ScenesManager:
    def __init__(self, game):
        self.scenes = {}
        self.game = game

    def register(self, scene_class, name):
        scene = scene_class(self.game)
        self.scenes[name] = scene

    def get_scene_by_name(self, name):
        try:
            return self.scenes[name]
        except:
            print("Scene " + name + " is not found")

