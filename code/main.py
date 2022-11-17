import pygame, sys
from button import Button
from settings import *
from level import Level
from enemy import Enemy
from player import Player
import json

scoreboard = {}

try:
    with open('score.json') as score_file:
        scoreboard = json.load(score_file)
except:
    pass

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("AngryCat")
font = pygame.font.Font('../Assets/font/Winkle-Regular.ttf',32)
main_sound = pygame.mixer.Sound('../audio/main.wav')
main_sound.set_volume(0.5)
main_sound.play(loops = -1)
clock = pygame.time.Clock()


BG = pygame.image.load('../Assets/start_menu/score.png')


def get_font(size):
    return pygame.font.Font("../Assets/font/Winkle-Regular.ttf", size)

def play():
    level = Level()
    while True:   

        if level.player_alive == False:
                gameOver()
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    level.toggle_menu()
            
        SCREEN.fill(WATER_COLOR)
        level.run()
        pygame.display.update()
        clock.tick(FPS)
    

def main_menu():
    while True:
        text_surf = font.render('65010773 Petch Tariyacharoen',False,'black')
        text_rect = text_surf.get_rect(center = (1280 - text_surf.get_width() , 720 - text_surf.get_height() - 5))
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(text_surf,text_rect)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("ANGRY CAT", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../Assets/button/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCORE_BUTTON = Button(image=pygame.image.load("../Assets/button/Options Rect.png"), pos=(640, 400), 
                            text_input="SCORE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../Assets/button/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    text_input()
                    #play()
                if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    score()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def score():
    level = Level()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            with open('score.json', 'r') as file:
                level.point = json.load(file)

            with open('score.json', 'w') as file:
                json.dump(level.point, file)
            
            
        pygame.display.update()

def gameOver():
    while True:
        font = get_font(75)
        text_surf = font.render('GAME OVER...',False,'black')
        text_rect = text_surf.get_rect(center = (640 , 350))
        level = Level()

        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(text_surf, text_rect)
        
        OVER_MOUSE_POS = pygame.mouse.get_pos()
        OVER_BACK = Button(image=None, pos=(640, 500), 
                            text_input="PLAY AGAIN", font=get_font(45), base_color="Black", hovering_color="Green")

        OVER_BACK.changeColor(OVER_MOUSE_POS)
        OVER_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OVER_BACK.checkForInput(OVER_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def text_input():
    level = Level()
    player_name = ''
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                       player_name = player_name[:-1]
                    elif event.key == pygame.K_RETURN and len(player_name) >= 1:
                        scoreboard[player_name] = level.point
                        play()
                    else:
                        player_name += event.unicode
        SCREEN.fill(UI_BG_COLOR)
        name_surf = font.render(player_name, False, 'gold')
        name_rect = name_surf.get_rect(center = (WIDTH // 2, HEIGTH // 2 ))
        pygame.draw.rect(SCREEN, UI_BG_COLOR, name_rect.inflate(20, 20))
        SCREEN.blit(name_surf, name_rect)
        pygame.display.update()

main_menu()