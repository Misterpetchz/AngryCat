import pygame 
from settings import *
from debug import debug

class Name:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()
        self.image = pygame.image.load('../Assets/start_menu/score.png')
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.font = pygame.font.Font(UI_FONT, 30)
        self.text = ''
        self.offset = 0
        self.count = 0

    def text_input(self, level, score):
        