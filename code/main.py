import pygame, sys
from setting import *
from level import Level
import json

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('AngryCat')
		self.clock = pygame.time.Clock()
		self.level = Level()

		#sound
		self.image_screen = pygame.image.load('../Assets/start_menu/screen.png')
		self.image_score =  pygame.image.load
		self.font = pygame.font.Font(UI_FONT, 10)
		self.rect = self.image_screen.get_rect(topleft = (0,0))
		main_sound = pygame.mixer.Sound('../audio/main.wav')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
		self.text_surf = self.font.render('65010773 Petch Tariyacharoen', False, TEXT_COLOR)
		self.text_surf = self.text_surf.get_rect(center = ((1280 // 2), 700))
		
		
	
	def run(self) :
			while True:
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_m:
							self.level.toggle_menu()

					self.screen.fill(WATER_COLOR)
					self.level.run()
					pygame.display.update()
					self.clock.tick(FPS)

	
class Homepage:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()

		self.start_menu = pygame.image.load('../Assets/start_menu/start.png')
		self.start_menu = pygame.transform.scale(self.start_menu,(WIDTH,HEIGHT))
		
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
			pygame.display.update()
			self.clock.tick(FPS)
			

if __name__ == '__main__':
	game = Game()
	game.run()