import pygame
import platform

DEFAULT_FONT = 'Noto Sans CJK SC'
if platform.system() == "Windows":
    DEFAULT_FONT = 'DFKai-SB'

def show_text(screen, string, color, size, position, align_hor="left", align_ver="top"):
    font = pygame.font.SysFont(DEFAULT_FONT, size)
    text = font.render(string, 1, color)
    text_size = font.size(string)

    aligned_x = position[0]
    aligned_y = position[1]

    if align_hor == "center":
        aligned_x -= text_size[0] / 2
    elif align_hor == "right":
        aligned_x -= text_size[0]

    if align_ver == "center":
        aligned_y -= text_size[1] / 2
    elif align_ver == "bottom":
        aligned_y -= text_size[1]

    screen.blit(text, (aligned_x, aligned_y))

def text_size(string, size):
    font = pygame.font.SysFont(DEFAULT_FONT, size)

    return font.size(string)


