import pygame
from game_settings import Settings


class Plane():

    def __init__(self, ai_settings, win):
        """initialize the plane and set position"""
        self.win = win
        self.ai_settings = ai_settings

        # load the plane and set rect
        self.plane_image = pygame.transform.rotate(pygame.image.load('images/medplane.png'), 360)
        self.rect = self.plane_image.get_rect()
        self.win_rect = win.get_rect()

        # Place the new plane on the center left
        self.rect.centery = self.win_rect.centery
        self.rect.midleft = self.win_rect.midleft

        # storing decimal to planes center
        self.center = float(self.rect.centery)
        self.center1 = float(self.rect.centerx)
        # move flg
        self.move_u = False
        self.move_d = False
        self.move_r = False
        self.move_l = False

    def update(self):
        """Update the ships position via the flag"""
        # update center of plane not rect
        if self.move_u and self.rect.bottom < self.win_rect.bottom:
            self.center += self.ai_settings.plane_speed
        if self.move_d and self.rect.top > 0:
            self.center -= self.ai_settings.plane_speed
        # update rectangle obj from.center
        self.rect.y = self.center
        if self.move_r and self.rect.right < self.win_rect.right:
            self.center1 += self.ai_settings.plane_speed
        if self.move_l and self.rect.left > 0:
            self.center1 -= self.ai_settings.plane_speed
            # update rectangle obj from.center
        self.rect.x = self.center1



    def blitm(self):
        """draw ship at current location"""
        self.win.blit(self.plane_image, self.rect)