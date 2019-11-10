import pygame
from pygame.sprite import Sprite

class Round(Sprite):
    """Manages rounds fire form the plane"""

    def __init__(self, ai_settings, win, plane):
        super(Round, self).__init__()
        self.win = win

        # create a round rectangle at 0,0 then set pos
        self.rect = pygame.Rect(0, 0, ai_settings.round_w,
                                ai_settings.round_h)
        self.rect.centery = plane.rect.centery
        self.rect.right = plane.rect.right
        self.rect.centerx = plane.rect.centerx


        # Store rounds pos as decimal
        self.x = float(self.rect.x)


        self.color = ai_settings.round_clr
        self.speed = ai_settings.round_speed

    def update(self):
        """move round to the right side of the screen"""
        # update pos of round
        self.x += self.speed
        # Update rect pos
        self.rect.x = self.x


    def draw_round(self):
        """paint round to screen"""
        pygame.draw.rect(self.win, self.color, self.rect)