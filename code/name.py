import pygame
from setting import *
from debug import debug


class Name:
    def __init__ (self):
        self.display_surf = pygame.display.get_surface()
        self.image = pygame.image.load('../Assets/start_menu/score.png')
        self.rect = self.image.get_rect(topleft = (0,0))
        self.font = pygame.font.Font(UI_FONT, 32)
        self.text = ''
        self.offset = 0
        self.count = 0

    def input(self, level, score):
        if level.death == True :
            for event in  pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pygame.K_RETURN:
                        score[self.text] = level.player.exp
                        
            