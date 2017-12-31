import pygame
from jumper.entity import Entity
from jumper.game_helper import show_text, text_size

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class TextInput(Entity):
    def __init__(self, color, font_size, size, position, text="", max_limit=10):
        self.color = color
        self.font_size = font_size
        self.size = size
        self.position = position
        self.text = text
        self.cursor = 0
        self.on_submit_func = None
        self.is_shift_down = False
        self.max_limit = max_limit
        self.reset_cursor()

    def reset_cursor(self):
        self.cursor_hidden = False
        self.cursor_blip = 0.0

    def get_text(self):
        return self.text

    def insert_text(self, char):
        self.reset_cursor()

        s = self.text
        c = self.cursor

        if len(s) + len(char) > self.max_limit: return

        self.text = s[:c] + char + s[c:]
        self.cursor += len(char)

    def delete_text(self, n=1):
        self.reset_cursor()

        s = self.text
        c = self.cursor

        if n > self.cursor:
            self.cursor = 0
            return s[c:]

        self.cursor -= n
        self.text = s[:c-n] + s[c:]

    def move_cursor(self, p):
        self.reset_cursor()

        c = self.cursor + p
        self.cursor = max(min(c, len(self.text)), 0)

    def on_submit(self, func):
        self.on_submit_func = func

    def submit(self):
        if self.on_submit_func != None:
            self.on_submit_func(self.text)

    def key_down(self, key):
        if key == pygame.K_RSHIFT or key == pygame.K_LSHIFT:
            self.is_shift_down = True

        char = ord('a')
        if self.is_shift_down:
            char = ord('A')
        if key == pygame.K_a: self.insert_text(chr(char + 0))
        if key == pygame.K_b: self.insert_text(chr(char + 1))
        if key == pygame.K_c: self.insert_text(chr(char + 2))
        if key == pygame.K_d: self.insert_text(chr(char + 3))
        if key == pygame.K_e: self.insert_text(chr(char + 4))
        if key == pygame.K_f: self.insert_text(chr(char + 5))
        if key == pygame.K_g: self.insert_text(chr(char + 6))
        if key == pygame.K_h: self.insert_text(chr(char + 7))
        if key == pygame.K_i: self.insert_text(chr(char + 8))
        if key == pygame.K_j: self.insert_text(chr(char + 9))
        if key == pygame.K_k: self.insert_text(chr(char + 10))
        if key == pygame.K_l: self.insert_text(chr(char + 11))
        if key == pygame.K_m: self.insert_text(chr(char + 12))
        if key == pygame.K_n: self.insert_text(chr(char + 13))
        if key == pygame.K_o: self.insert_text(chr(char + 14))
        if key == pygame.K_p: self.insert_text(chr(char + 15))
        if key == pygame.K_q: self.insert_text(chr(char + 16))
        if key == pygame.K_r: self.insert_text(chr(char + 17))
        if key == pygame.K_s: self.insert_text(chr(char + 18))
        if key == pygame.K_t: self.insert_text(chr(char + 19))
        if key == pygame.K_u: self.insert_text(chr(char + 20))
        if key == pygame.K_v: self.insert_text(chr(char + 21))
        if key == pygame.K_w: self.insert_text(chr(char + 22))
        if key == pygame.K_x: self.insert_text(chr(char + 23))
        if key == pygame.K_y: self.insert_text(chr(char + 24))
        if key == pygame.K_z: self.insert_text(chr(char + 25))
        if key == pygame.K_SPACE: self.insert_text(' ')
        if key == pygame.K_GREATER: self.insert_text('.')
        if key == pygame.K_BACKSPACE: self.delete_text()
        if key == pygame.K_RIGHT: self.move_cursor(1)
        if key == pygame.K_LEFT: self.move_cursor(-1)
        if key == pygame.K_RETURN: self.submit()

    def key_up(self, key):
        if key == pygame.K_RSHIFT or key == pygame.K_LSHIFT:
            self.is_shift_down = False

    def update(self, delta):
        self.cursor_blip += delta

        if self.cursor_blip > 0.5:
            self.cursor_hidden = not self.cursor_hidden
            self.cursor_blip %= 0.5

    def render(self, surface):
        self._render_background(surface)
        self._render_text(surface)

        if not self.cursor_hidden:
            self._render_cursor(surface)

    def _render_background(self, surface):
        x, y = self.position
        w, h = self.size

        pygame.draw.rect(surface, WHITE, (x, y, w, h))
        pygame.draw.rect(surface, BLACK, (x, y, w, h), 10)

    def _render_text(self, surface):
        x = self.position[0] + self.size[0]/2
        y = self.position[1] + self.size[1]/2

        show_text(surface,
                  self.text,
                  self.color,
                  self.font_size,
                  (x, y),
                  align_hor="center",
                  align_ver="center")

    def _render_cursor(self, surface):
        c = self.cursor
        t_w, t_h = text_size(self.text[:c], self.font_size)
        a_w, a_h = text_size(self.text, self.font_size)

        x = self.position[0] + (self.size[0] - a_w)/2 + t_w
        y = self.position[1] + self.size[1] * 0.3
        w, h = 1, self.font_size

        pygame.draw.rect(surface, self.color, (x, y, w, h), 3)
