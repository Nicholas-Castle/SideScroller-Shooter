import pygame

class Settings():
    """Store all the settings for the game here"""

    def __init__(self):
        """init the games settings"""
        self.bg_image = pygame.image.load('images/Mountains_PS.bmp')
        self.win_width = 800
        self.win_height = 600

        # plane settings
        self.plane_speed = 1

        # Bullet Settings
        self.round_speed = 2
        self.round_w = 11
        self.round_h = 5
        self.round_clr = 50, 50, 50
        self.num_rounds_on_screen = 5