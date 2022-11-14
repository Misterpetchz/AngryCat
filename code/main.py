import pygame, sys
from setting import *
from level import Level
import button

#setup
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('AngryCat')
gameIcon = pygame.image.load('../Assets/icon/angryCat.jfif')
pygame.display.set_icon(gameIcon)


#button
homepage_start_button = pygame.image.load('../Assets/button/start1.png')
homepage_score_button = pygame.image.load('../Assets/button/score.png')
homepage_exit_button = pygame.image.load('../Assets/button/exit.png')

homepage_start = button.Button(WIDTH // 2 - 130, HEIGHT // 2 - 120, homepage_start_button,1)
homepage_score = button.Button(WIDTH // 2 - 120, HEIGHT // 2 - 100, homepage_score_button,1)
homepage_exit = button.Button(WIDTH // 2 - 110, HEIGHT // 2 - 180, homepage_exit_button,1)


class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.clock = pygame.time.Clock()
		self.level = Level()
		self.Homepage.homepage_active = True
		#sound
		main_sound = pygame.mixer.Sound('../audio/main.wav')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
		
		
	
	def run(self) :
			while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							sys.exit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_m:
								self.level.toggle_menu()

					screen.fill(WATER_COLOR )
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