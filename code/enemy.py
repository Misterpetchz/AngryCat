import pygame
from setting import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups):

        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.import_grahpics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def import_grahpics(self,name):
        self.animations = {'idle':[], 'move':[], 'attack':[]}
        main_path = f'../Assets/monster/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
