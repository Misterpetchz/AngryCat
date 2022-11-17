import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint, random
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
font = pygame.font.Font('../Assets/font/Winkle-Regular.ttf', 32)
screen = pygame.display.set_mode((1280,720))

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False
		self.time_spawn = pygame.time.get_ticks()
		self.update_time_spawn = 0

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
		self.enemies_max = 15
		self.enemies = 0
		self.player_alive = True

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()
		self.magic_player = MagicPlayer(self.animation_player)

		self.point = 0

	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('../map/new1_floorblock.csv'),
			'entities': import_csv_layout('../map/true1_entities.csv')
		}

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')

						if style == 'entities':
							if col == '394':
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic)
							else:
								pass
								#if col == '390': monster_name = 'beetle'
								#elif col == '391': monster_name = 'maggot'
								#else: monster_name = 'wyrm'
								#Enemy(
								#	monster_name,
								#	(x,y),
								#	[self.visible_sprites,self.attackable_sprites],
								#	self.obstacle_sprites,
									#self.damage_player,
								#	self.trigger_death_particles,
									#self.add_exp)

	def create_attack(self):
		
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def create_magic(self,style,strength,cost):

		if style == 'crescent':
			self.magic_player.crescent(self.player,cost,[self.visible_sprites,self.attack_sprites])

		if style == 'fireball':
					self.magic_player.fireball(self.player,cost,[self.visible_sprites,self.attack_sprites])	

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'enemy':
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)

	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])

	def trigger_death_particles(self,pos,particle_type):

		self.animation_player.create_particles(particle_type,pos,self.visible_sprites)
		monster_data[particle_type]['health'] += 0.5
		monster_data[particle_type]['damage'] += 0.75
		monster_data[particle_type]['speed'] += 0.01
		self.point += 20

	def add_exp(self,amount):

		self.player.exp += amount

	def toggle_menu(self):

		self.game_paused = not self.game_paused 

	def spawn(self):
		layouts = {
			'spawn': import_csv_layout('../map/finally_entities.csv')
		}
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'spawn':
							rand = randint(1,5)
							if col == '391' and self.enemies <= self.enemies_max:
								if rand == 1 or rand == 2: 
									self.enemies += 1
									Enemy(
										'beetle',
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player,
										self.trigger_death_particles,
										self.add_exp)
								if rand == 2 or rand == 3:
									self.enemies += 1
									Enemy(
										'maggot',
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player,
										self.trigger_death_particles,
										self.add_exp)
								if rand == 5:
									self.enemies += 1
									Enemy(
										'wyrm',
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player,
										self.trigger_death_particles,
										self.add_exp)

									# add another type

	def check_player_death(self):
		if self.player.health <= 0:
			self.player_alive = False
			
	# def drop_item(self,pos):
	#	 self.image = pygame.image.load('../Assets/potion/health_potion.png').convert_alpha()
	#	 self.rect = self.image.get_rect(center =(pos[0],pos(1)))
	
	def show_score(self):
		text_surf = font.render('Score : ' + str(self.point), True, (255,255,255))
		text_rect = text_surf.get_rect(center = (WIDTH - text_surf.get_width() - 5, 25))
		screen.blit(text_surf,text_rect)


	def run(self):
		
		self.visible_sprites.custom_draw(self.player)
		self.ui.display(self.player)
		self.time_spawn = pygame.time.get_ticks()
		self.show_score()
		if self.time_spawn - self.update_time_spawn >= 30000:
			self.enemies_max += 15
			self.update_time_spawn = self.time_spawn
			self.enemies = 0
		self.spawn()
		#print(self.time_spawn)
		self.check_player_death()
		
		if self.game_paused:
			self.upgrade.display()
		else:
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.player_attack_logic()
		

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../Assets/tilemap/castlefarm.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
