import pygame
from player import Player

class Items(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.sprite_type = 'item'
        self.image = pygame.image.load('../Assets/potion/health_potion.png')
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0],pos[1]) 

        