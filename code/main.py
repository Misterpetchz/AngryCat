import pygame, sys
from setting import *
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('AngryCat')
		self.clock = pygame.time.Clock()
		self.level = Level()

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
				self.clock.tick(60)

if __name__ == '__main__':
	game = Game()
	game.run()