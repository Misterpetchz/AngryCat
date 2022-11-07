from email.mime import image
from entity import Entity
import pygame 
from setting import *
from support import import_folder
from entity import Entity

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_magic):
		super().__init__(groups)
		self.image = pygame.image.load('../Assets/player/down_idle/down_idle.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-20)

		#graphics setup
		self.import_player_asset()
		self.status = 'down'

		#movement 
		self.speed = 5
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None
		self.obstacle_sprites = obstacle_sprites
		
		#weapon
		self.create_attack = create_attack
		self.destroy_attack = destroy_attack
		self.weapon_index = 0
		self.weapon = list(weapon_data.keys())[self.weapon_index]
		self.switch_duration_cooldown = 200
		self.can_switch_weapon = True
		#self.weapon_switch_time = None
		

		#skill
		self.create_magic = create_magic
		self.magic_index = 0
		self.magic = list(magic_data.keys())[self.magic_index]
		self.can_switch_magic = True
		self.magic_switch_time = None

		#stats
		self.stats = {'health' : 100, 'energy' : 60, 'attack' : 10, 'magic' : 4, 'speed' : 5}
		self.health = self.stats['health'] 
		self.energy = self.stats['energy'] 
		self.exp = 123
		self.speed = self.stats['speed']


	def import_player_asset(self):
		character_path = '../Assets/player/'
		self.animations = {'up': [], 'down' : [], 'left' : [], 'right': [],
					'up_idle' : [], 'down_idle': [], 'left_idle' : [], 'right_idle' : [],
					'up_attack' : [], 'down_attack' : [], 'left_attack' : [], 'right_attack' : []}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()

			#movement input
			if keys[pygame.K_UP]:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN]:
				self.direction.y = 1
				self.status = 'down'
			else :
				self.direction.y = 0

			if keys[pygame.K_LEFT]:
				self.direction.x = -1
				self.status = 'left'
			elif keys[pygame.K_RIGHT]:
				self.direction.x = 1
				self.status = 'right'
			else :
				self.direction.x = 0

			#attack input
			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				self.create_attack()

			#skill input
			if keys[pygame.K_LCTRL]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				style = list(magic_data.keys())[self.magic_index]
				strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
				cost = list(magic_data.values())[self.magic_index]['cost']
				self.create_magic(style,strength,cost)

			if keys[pygame.K_z] and self.can_switch_magic:
				self.can_switch_magic = False
				self.magic_switch_time = pygame.time.get_ticks()
				if self.magic_index < len(list(magic_data.keys())) - 1:
					self.magic_index += 1
				else :
					self.magic_index = 0

				self.magic = list(magic_data.keys())[self.magic_index]

	def get_status(self):

		#idle status
		if self.direction.x == 0 and self.direction.y == 0 :
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					#overwrite idle
					self.status = self.status.replace('_idle', '_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack' ,'')


	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attack_time:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False
				self.destroy_attack()

		if not self.can_switch_magic:
			if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
				self.can_switch_magic = True

	def animate(self):
		animation = self.animations[self.status]

		#loop over the frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		#set the image
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 2), int(self.image.get_height() * 2)))
		self.move(self.speed)