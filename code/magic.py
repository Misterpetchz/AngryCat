import pygame
from settings import *
from random import randint

class MagicPlayer:
	def __init__(self,animation_player):
		self.animation_player = animation_player
		self.sounds = {
		'crescent': pygame.mixer.Sound('../audio/ching_crescent.wav'),
		'fireball':pygame.mixer.Sound('../audio/Fireball.wav')
		}


	def crescent(self,player,cost,groups):
		if player.energy >= cost:
			player.energy -= cost
			self.sounds['crescent'].play()

			if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
			elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
			elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
			else: direction = pygame.math.Vector2(0,1)

			for i in range(1,6):
				if direction.x: #horizontal
					offset_x = (direction.x * i) * TILESIZE
					x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('crescent',(x,y),groups)
				else: # vertical
					offset_y = (direction.y * i) * TILESIZE
					x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('crescent',(x,y),groups)

	def fireball(self,player,cost,groups):
		if player.energy >= cost:
			player.energy -= cost
			self.sounds['fireball'].play()

			if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
			elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
			elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
			else: direction = pygame.math.Vector2(0,1)

			for i in range(1,6):
				if direction.x: #horizontal
					offset_x = (direction.x * i) * TILESIZE
					x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('fireball',(x,y),groups)
				else: # vertical
					offset_y = (direction.y * i) * TILESIZE
					x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('fireball',(x,y),groups)