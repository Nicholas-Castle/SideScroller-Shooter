import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Represents the enemy planes"""

    def __init__(self, ai_settings, win):
        """Initialize the starting pos for the enemy"""
        super(Enemy, self).__init__()
        self.win = win
        self.ai_settings = ai_settings

        # Load plane image and set rect
        self.image = pygame.transform.rotate(pygame.image.load('images/plane.png'), 180)
        self.rect = self.image.get_rect()

        # Place enemy top right of screen
        self.rect.x = 700
        self.rect.y = 20

        # Store pos of enemy plane
        self.x = float(self.rect.x)

    def blitm(self):
        """paint plane to screen at current pos"""
        self.win.blit(self.image, self.rect)
