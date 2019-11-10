import sys
import pygame
from round import Round
from game_settings import Settings
from enemy_planes import Enemy

def get_num_col(ai_settings, plane_h, enemy_h,):
    """See how much space is in a column"""
    avail_space_x = ai_settings.win_height - ( 2 * enemy_h) - plane_h
    num_cols = int(avail_space_x)/ (2 * enemy_h)
    return num_cols

def get_num_planes(ai_settings, enemy_w):
    """determine num of planes on y axis"""
    space_avail_y = ai_settings.win_width - 4 * enemy_w
    num_enemies_y = int(space_avail_y / 2 + enemy_w)
    return num_enemies_y

def create_plane(ai_settings, win, enemies, num_enemies, row_cols):
    """Make planes and place in column"""
    enemy = Enemy(ai_settings, win)
    enemy_w = enemy.rect.width
    enemy = Enemy(ai_settings, win)
    enemy.y = enemy_w + 2 * enemy_w * num_enemies
    enemy.rect.y = enemy.y
    
    enemies.add(enemy)


def make_enemies(ai_settings, win, enemies):
    """make a group of enemies"""
    # add space between enemies in row
    # Make space equal to half and enemy
    enemy = Enemy(ai_settings, win)
    num_enemies_y = get_num_planes(ai_settings, enemy.rect.width)

    # make row od enemies
    for num_enemy in range(num_enemies_y):
        # makes plane and put plane in pos
        create_plane(ai_settings, win, enemies, num_enemy)


def ck_keydown_evnt(e, ai_settings, win, plane, rounds):
    """respond to key press"""
    if e.key == pygame.K_UP:
        plane.move_u = True
    elif e.key == pygame.K_DOWN:
        plane.move_d = True
    elif e.key == pygame.K_RIGHT:
        plane.move_r = True
    elif e.key == pygame.K_LEFT:
        plane.move_l = True
    elif e.key == pygame.K_SPACE:
        shoot_round(ai_settings, win, plane, rounds)

def shoot_round(ai_settings, win, plane, rounds):
    """shoot a round if !limit"""
    if len(rounds) < ai_settings.num_rounds_on_screen:
        new_round = Round(ai_settings, win, plane)
        rounds.add(new_round)

def ck_keyup_evnt(e, plane):
    """respond to key press"""
    if e.key == pygame.K_UP:
        plane.move_u = False
    elif e.key == pygame.K_DOWN:
        plane.move_d = False
    elif e.key == pygame.K_RIGHT:
        plane.move_r = False
    elif e.key == pygame.K_LEFT:
        plane.move_l = False

def ck_evt(ai_settings, win, plane, rounds):
    """respond to key press"""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYUP:
            ck_keyup_evnt(e, plane)
        elif e.type == pygame.KEYDOWN:
            ck_keydown_evnt(e, ai_settings, win, plane, rounds)


def update_win(ai_settings, win, plane, enemies, rounds):
    """Updates images and flips screen"""
    # draw plane to screen

    # Draw background to screen
    win.blit(ai_settings.bg_image, (0, 0))
    for bullet in rounds.sprites():
        bullet.draw_round()
    plane.blitm()
    enemies.draw(win)

    # Make recent screen visible
    pygame.display.flip()

def update_rounds(rounds):
    """deletes old rounds and updates position of rounds"""
    ai_settings = Settings()
    # Update pos round
    for bullet in rounds.copy():
        if bullet.rect.left >= ai_settings.win_width:
            rounds.remove(bullet)
        print(len(rounds))
