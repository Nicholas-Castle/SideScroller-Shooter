import pygame
from plane import Plane
from game_settings import Settings
from enemy_planes import Enemy
import game_funct as game_f
from pygame.sprite import Group

def start_game():
    # start the game and make a screen object
    pygame.init()
    ai_settings = Settings()
    win = pygame.display.set_mode(
        (ai_settings.win_width, ai_settings.win_height))
    pygame.display.set_caption("The Gauntlet")

    # draw a plane so the screen
    plane = Plane(ai_settings, win)
    # Creates group to store rounds and enemies
    rounds = Group()
    enemies = Group()
    # create an enemy

    game_f.make_enemies(ai_settings, win, enemies)


    # Main game loop
    while True:
        game_f.ck_evt(ai_settings, win, plane, rounds)
        plane.update()
        rounds.update()
        game_f.update_rounds(rounds)
        game_f.update_win(ai_settings, win, plane, enemies, rounds)

start_game()

