from pygame import Surface
from jumper.entity import Entity
from jumper.entities.player import Player
from jumper.stages.stage1 import Stage1

class Environment(Entity):
    def __init__(self, scene):
        self.scene = scene
        self.stage = Stage1()
        self.player = Player(self, (200, 200))
        self.level = 0.0

    def get_scene(self):
        return self.scene

    def get_level(self):
        return self.level

    def player_jump(self):
        self.player.jump()

    def update(self, delta):
        self.player.update(delta)

    def render(self, screen):
#        background = pygame.transform.scale(R.get_image("dirt"), self.game.get_bound())
#        screen.blit(background, (0, 0))
        screen.fill(self.stage.get_background())

        self.player.render(screen)


