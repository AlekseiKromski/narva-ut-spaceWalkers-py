import pygame
from libs.ballClass import Ball
import os
class Player:
    player_X = 600
    player_Y = 400
    shot = False
    view = 'right'
    shotDistance = 150
    ball = ''
    ballInit = False
    image = [
        [os.path.join('textures', 'player', 'main_top.png')],
        [os.path.join('textures', 'player', 'main_right.png')],
        [os.path.join('textures', 'player', 'main_bottom.png')],
        [os.path.join('textures', 'player', 'main_left.png')],
    ]
    surf = pygame.image.load(image[1][0])
    
    def __init__(self, screen):
        self.screen = screen
        self.spawn()

    def spawn(self):
        self.screen.blit(self.surf, (self.player_X,self.player_Y))

    def keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_X -= 10
            self.view = 'left'
            self.__setSurf(self.image[3][0]) 
        if keys[pygame.K_RIGHT]:
            self.player_X += 10
            self.view = 'right'
            self.__setSurf(self.image[1][0]) 
        if keys[pygame.K_UP]:
            self.player_Y -= 10 
            self.view = 'top'  
            self.__setSurf(self.image[0][0]) 
        if keys[pygame.K_DOWN]:
            self.player_Y += 10 
            self.view = 'bottom'
            self.__setSurf(self.image[2][0]) 
        if keys[pygame.K_SPACE]:
            if not self.shot:
                self.shot = True
    def ballActionMethod(self, bots):
        if self.shot:
            if not self.ballInit:
                if self.view == 'right':
                    self.ball = Ball(self.view, self.player_X + self.shotDistance, self.player_X, self.player_Y, self.screen)
                if self.view == 'left':
                    self.ball = Ball(self.view, self.player_X - self.shotDistance, self.player_X, self.player_Y, self.screen)
                if self.view == 'bottom':
                    self.ball = Ball(self.view, self.player_Y + self.shotDistance, self.player_X, self.player_Y, self.screen)
                if self.view == 'top':
                    self.ball = Ball(self.view, self.player_Y - self.shotDistance, self.player_X, self.player_Y, self.screen)
                self.ballInit = True
            else:
                if self.ball.isDestroyed:
                    self.shot = False
                    self.ballInit = False
                    del self
                else:
                    bots = self.ball.strike(bots)
        return bots
    def __setSurf(self, img):
        self.surf = pygame.image.load(img)
