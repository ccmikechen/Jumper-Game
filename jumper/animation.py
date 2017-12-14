import pygame
from jumper.entity import Entity

class Animation(Entity):
    def __init__(self, frame_size, time, position, size):
        self.frame_size = frame_size
        self.time = time
        self.progress = 0
        self.is_playing = False
        self.loops = 0
        self.position = position
        self.size = size

    def get_frame(self, index):
        raise NotImplementedError()

    def set_position(self, new_pos):
        self.position = new_pos

    def play(self, loops=0):
        self.loops = loops
        self.is_playing = True

    def pause(self):
        self.is_playing = False

    def stop(self):
        self.is_playing = False
        self.progress = 0

    def update(self, delta):
        if self.is_playing:
            self.progress += delta

            if self.progress > self.time:
                self.stop()
                if self.loops < 0:
                    self.play(self.loops)
                elif self.loops > 0:
                    self.play(self.loops - 1)

    def render(self, screen):
        if self.is_playing:
            index = int(self.frame_size * self.progress / self.time)

            frame = self.get_frame(index)
            frame = pygame.transform.scale(frame, self.size)

            screen.blit(frame, self.position)
