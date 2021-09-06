import pygame
from libs.ballClass import Ball
class Player:
    player_X = 100
    player_Y = 50
    shot = False
    view = 'right'
    shotDistance = 150
    ball = ''
    ballInit = False
    
    def __init__(self, screen):
        self.screen = screen
        self.spawn()

    def spawn(self):
        self.player = pygame.Rect(self.player_X, self.player_Y, 20, 20)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player)

    def keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_X -= 10
            self.view = 'left'
        if keys[pygame.K_RIGHT]:
            self.player_X += 10
            self.view = 'right'
        if keys[pygame.K_UP]:
            self.player_Y -= 10 
            self.view = 'top'  
        if keys[pygame.K_DOWN]:
            self.player_Y += 10 
            self.view = 'bottom'
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
