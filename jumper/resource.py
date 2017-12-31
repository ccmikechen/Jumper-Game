import pygame
from jumper.sprite_sheet import SpriteSheet

class Resource:
    def __init__(self):
        self.images = {}
        self.sprite_sheets = {}
        self.sounds = {}
        self.music = {}

    def load(self):
        print("Loading resources...")

        # Player
        ninja = pygame.image.load("jumper/images/ninja.png").convert_alpha()
        ninja_sprite_sheet = SpriteSheet(pygame.transform.scale(ninja, (1014, 1014)),
                                         (78, 79))
        self.sprite_sheets["ninja"] = ninja_sprite_sheet

        # Monster
        slime = pygame.image.load("jumper/images/slime.png").convert_alpha()
        slime_sprite_sheet = SpriteSheet(slime, (32, 32))
        self.sprite_sheets["slime"] = slime_sprite_sheet

        # Home
        home_bg = pygame.image.load("jumper/images/home_bg.jpg")
        home_bg_size = home_bg.get_rect().size
        home_bg = pygame.transform.scale(home_bg, (home_bg_size[0] * 2, home_bg_size[1] * 2))

        self.images["home_bg"] = home_bg

        title = pygame.image.load("jumper/images/title.png").convert_alpha()
        tx, ty = title.get_rect().size
        self.images["title"] = pygame.transform.scale(title, (int(tx * 1.5), int(ty * 1.5)))

        # Menu
        menu_bg = pygame.image.load("jumper/images/menu_bg.jpg")
        mx, my = home_bg.get_rect().size
        self.images["menu_bg"] = pygame.transform.scale(menu_bg, (int(mx * (960 / my)), 960))

        menu_option = pygame.image.load("jumper/images/menu_option.png")
        self.images["menu_option"] = pygame.transform.scale(menu_option, (500, 120)).convert_alpha()

        lock = pygame.image.load("jumper/images/lock.png")
        self.images["lock"] = pygame.transform.scale(lock, (100, 100)).convert_alpha()

        # Ranking
        ranking_bg = pygame.image.load("jumper/images/kanban.png")
        self.images["ranking_bg"] = pygame.transform.scale(ranking_bg, (600, 900)).convert_alpha()

        black_board = pygame.image.load("jumper/images/black_board.jpg")
        self.images["black_board"] = black_board

        # Stage1 background
        stage1_bg = pygame.image.load("jumper/images/stage1_bg.jpg")
        stage1_bg_size = stage1_bg.get_rect().size
        stage1_bg = pygame.transform.scale(stage1_bg,
                                           (stage1_bg_size[0] * 3, stage1_bg_size[1] * 3))
        self.images["stage1_bg"] = stage1_bg

        # Stage2 background
        stage2_bg = pygame.image.load("jumper/images/stage2_bg.png")
        stage2_bg_size = stage2_bg.get_rect().size
        stage2_bg = pygame.transform.scale(stage2_bg,
                                           (stage2_bg_size[0] * 2, stage2_bg_size[1] * 2))
        self.images["stage2_bg"] = stage2_bg

        # Platforms
        self.images["platform1"] = pygame.image.load("jumper/images/platform1.png")

        # Item1
        item1_sprite_sheet = SpriteSheet(pygame.image.load("jumper/images/item1.png").convert_alpha(),
                                         (24, 24))
        self.sprite_sheets["item1"] = item1_sprite_sheet

        self.images["spring_shoes"] = item1_sprite_sheet.image_at(0, 3)
        self.images["gravity_reducer"] = item1_sprite_sheet.image_at(14, 9)

        # Item2 (weapon)
        item2_sprite_sheet = SpriteSheet(pygame.image.load("jumper/images/item2.png").convert_alpha(),
                                         (18, 18))
        self.sprite_sheets["item2"] = item2_sprite_sheet

        self.images["bb_gun"] = item2_sprite_sheet.image_at(0, 3)
        self.images["bb_shotgun"] = item2_sprite_sheet.image_at(3, 3)
        self.images["bb_wavegun"] = item2_sprite_sheet.image_at(7, 3)

#        self.sounds["eat"] = pygame.mixer.Sound("snake/music/eat.wav")

#        self.music["menu"] = "snake/music/menubgm.mp3"

        print("Resources loaded.")

    def get_image(self, name):
        try:
            return self.images[name]
        except:
            print("Image " + name + " not found")

    def get_sprite_sheet(self, name):
        try:
            return self.sprite_sheets[name]
        except:
            print("Sprite sheet " + name + " not found")

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
