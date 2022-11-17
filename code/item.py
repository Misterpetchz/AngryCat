import pygame
from pygame.locals import *
from player import Player
from random import randint

class Itembox():
    def __init__(self,x,y):
        self.screen = pygame.display.set_mode((1280,720))
        self.image = pygame.image.load('../Assets/potion/health_potion.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def draw(self):
        self.screen.blit(self.x, self.y)

        