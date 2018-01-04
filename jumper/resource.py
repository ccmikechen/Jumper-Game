import pygame
from jumper.sprite_sheet import SpriteSheet
import os
import platform

def path(p):
    if platform.system() == "Windows":
        return p.replace("/", "\\")
    else:
        return p

class Resource:
    def __init__(self):
        self.images = {}
        self.sprite_sheets = {}
        self.sounds = {}
        self.music = {}
        self.music_playing = None

    def load(self):
        print("Loading resources...")

        self._load_images()
        self._load_sounds()
        self._load_music()

    def _load_images(self):
        # Player
        ninja = pygame.image.load(path("jumper/images/ninja.png")).convert_alpha()
        ninja_sprite_sheet = SpriteSheet(pygame.transform.scale(ninja, (1014, 1014)),
                                         (78, 79))
        self.sprite_sheets["ninja"] = ninja_sprite_sheet

        # Monster
        slime = pygame.image.load(path("jumper/images/slime.png")).convert_alpha()
        slime_sprite_sheet = SpriteSheet(slime, (32, 32))
        self.sprite_sheets["slime"] = slime_sprite_sheet

        # Home
        home_bg = pygame.image.load(path("jumper/images/home_bg.jpg"))
        home_bg_size = home_bg.get_rect().size
        home_bg = pygame.transform.scale(home_bg, (home_bg_size[0] * 2, home_bg_size[1] * 2))

        self.images["home_bg"] = home_bg

        title = pygame.image.load(path("jumper/images/title.png")).convert_alpha()
        tx, ty = title.get_rect().size
        self.images["title"] = pygame.transform.scale(title, (int(tx * 1.5), int(ty * 1.5)))

        # Menu
        menu_bg = pygame.image.load(path("jumper/images/menu_bg.jpg"))
        mx, my = home_bg.get_rect().size
        self.images["menu_bg"] = pygame.transform.scale(menu_bg, (int(mx * (960 / my)), 960))

        menu_option = pygame.image.load(path("jumper/images/menu_option.png"))
        self.images["menu_option"] = pygame.transform.scale(menu_option, (500, 120)).convert_alpha()

        lock = pygame.image.load(path("jumper/images/lock.png"))
        self.images["lock"] = pygame.transform.scale(lock, (100, 100)).convert_alpha()

        # Ranking
        ranking_bg = pygame.image.load(path("jumper/images/kanban.png"))
        self.images["ranking_bg"] = pygame.transform.scale(ranking_bg, (600, 900)).convert_alpha()

        black_board = pygame.image.load(path("jumper/images/black_board.jpg"))
        self.images["black_board"] = black_board

        # Stage1 background
        stage1_bg = pygame.image.load(path("jumper/images/stage1_bg.jpg"))
        stage1_bg_size = stage1_bg.get_rect().size
        stage1_bg = pygame.transform.scale(stage1_bg,
                                           (stage1_bg_size[0] * 3, stage1_bg_size[1] * 3))
        self.images["stage1_bg"] = stage1_bg

        # Stage2 background
        stage2_bg = pygame.image.load(path("jumper/images/stage2_bg.jpg"))
        stage2_bg_size = stage2_bg.get_rect().size
        stage2_bg = pygame.transform.scale(stage2_bg,
                                           (stage2_bg_size[0] * 2, stage2_bg_size[1] * 2))
        self.images["stage2_bg"] = stage2_bg

        # Stage3 background
        stage3_bg = pygame.image.load(path("jumper/images/stage3_bg.png"))
        stage3_bg_size = stage3_bg.get_rect().size
        stage3_bg = pygame.transform.scale(stage3_bg,
                                           (stage3_bg_size[0] * 2, stage3_bg_size[1] * 2))
        self.images["stage3_bg"] = stage3_bg

        # Stage4 background
        stage4_bg = pygame.image.load(path("jumper/images/stage4_bg.jpg"))
        stage4_bg_size = stage4_bg.get_rect().size
        stage4_bg = pygame.transform.scale(stage4_bg,
                                           (stage4_bg_size[0] * 2, stage4_bg_size[1] * 2))
        self.images["stage4_bg"] = stage4_bg

        # Stage5 background
        stage5_bg = pygame.image.load(path("jumper/images/stage5_bg.jpg"))
        stage5_bg_size = stage5_bg.get_rect().size
        stage5_bg = pygame.transform.scale(stage5_bg,
                                           (stage5_bg_size[0] * 2, stage5_bg_size[1] * 2))
        self.images["stage5_bg"] = stage5_bg

        # Platforms
        self.images["platform1"] = pygame.image.load(path("jumper/images/platform1.png"))
        self.images["platform2"] = pygame.image.load(path("jumper/images/platform2.png"))
        self.images["platform3"] = pygame.image.load(path("jumper/images/platform3.png"))

        # Item1
        item1_sprite_sheet = SpriteSheet(pygame.image.load(path("jumper/images/item1.png")).convert_alpha(),
                                         (24, 24))
        self.sprite_sheets["item1"] = item1_sprite_sheet

        self.images["spring_shoes"] = item1_sprite_sheet.image_at(0, 3)
        self.images["gravity_reducer"] = item1_sprite_sheet.image_at(14, 9)
        self.images["coin"] = item1_sprite_sheet.image_at(13, 12)

        # Item2 (weapon)
        item2_sprite_sheet = SpriteSheet(pygame.image.load(path("jumper/images/item2.png")).convert_alpha(),
                                         (18, 18))
        self.sprite_sheets["item2"] = item2_sprite_sheet

        self.images["bb_gun"] = item2_sprite_sheet.image_at(0, 3)
        self.images["bb_shotgun"] = item2_sprite_sheet.image_at(3, 3)
        self.images["bb_wavegun"] = item2_sprite_sheet.image_at(7, 3)

    def _load_sounds(self):
        self.sounds["select"] = pygame.mixer.Sound(path("jumper/sounds/Evasion1.ogg"))
        self.sounds["go_back"] = pygame.mixer.Sound(path("jumper/sounds/go_back.wav"))
        self.sounds["confirm"] = pygame.mixer.Sound(path("jumper/sounds/Bow2.ogg"))
        self.sounds["change_scene"] = None
        self.sounds["count"] = pygame.mixer.Sound(path("jumper/sounds/Bell3.ogg"))

        self.sounds["jump"] = pygame.mixer.Sound(path("jumper/sounds/Jump1.ogg"))
        self.sounds["bb_gun"] = pygame.mixer.Sound(path("jumper/sounds/bb_gun.wav"))
        self.sounds["shotgun"] = pygame.mixer.Sound(path("jumper/sounds/shotgun.wav"))
        self.sounds["wave_gun"] = pygame.mixer.Sound(path("jumper/sounds/wave_gun.wav"))
        self.sounds["get_item"] = pygame.mixer.Sound(path("jumper/sounds/Item3.ogg"))

        self.sounds["player_death"] = pygame.mixer.Sound(path("jumper/sounds/player_death.wav"))
        self.sounds["slime_death"] = pygame.mixer.Sound(path("jumper/sounds/slime_death.wav"))
        self.sounds["slime_step"] = pygame.mixer.Sound(path("jumper/sounds/slime_step.wav"))

    def _load_music(self):
        self.music["home"] = path("jumper/music/home.ogg")
        self.music["stage1"] = path("jumper/music/stage1.ogg")
        self.music["stage2"] = path("jumper/music/stage2.ogg")
        self.music["stage3"] = path("jumper/music/stage3.ogg")
        self.music["stage4"] = path("jumper/music/stage4.ogg")
        self.music["stage5"] = path("jumper/music/stage5.ogg")

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

    def play_sound(self, name, volume=0.5):
        try:
            self.sounds[name].set_volume(volume)
            self.sounds[name].play()
            pass
        except:
            print("Sound " + name + " not found")

    def play_music(self, name, loops=0, replay=False):
        if not replay and self.music_playing == name:
            return

        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(loops=loops)
            self.music_playing = name
        except:
            print("Music " + name + " not found")
            pygame.quit()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_playing = None

R = Resource()
