import pygame

class Resource:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.music = {}

    def load(self):
        print("Loading resources...")

#        self.images["blood"] = pygame.image.load("snake/images/blood.png").convert_alpha()
#        self.images["dirt"] = pygame.image.load("snake/images/dirt.png")

#        self.sounds["eat"] = pygame.mixer.Sound("snake/music/eat.wav")

#        self.music["menu"] = "snake/music/menubgm.mp3"

        print("Resources loaded.")

    def get_image(self, name):
        try:
            return self.images[name]
        except:
            print("Image " + name + " not found")

    def get_sound(self, name):
        try:
            return self.sounds[name]
        except:
            print("Sound " + name + " not found")
            pygame.quit()

    def play_music(self, name, loops=0):
        try:
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(loops=loops)
        except:
            print("Music " + name + " not found")
            pygame.quit()

R = Resource()
