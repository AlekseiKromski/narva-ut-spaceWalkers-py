import pygame
import math
class Bot:
    def __init__(self, x, y, screen):
        self.posx,self.posy, self.step, self.screen = x, y, 10, screen
        self.spawn()
        self.isRunMove = True

    def spawn(self):
        self._self = pygame.Rect(self.posx, self.posy, 20, 20)
        pygame.draw.rect(self.screen, (0,0,255), self._self)
    def calculate(self, player_pos):
        if self.isRunMove:
            #Find y distance
            distance_y = math.fabs(self.posy - player_pos[1])

            #Find x distance
            distance_x = math.fabs(self.posx - player_pos[0])

            if distance_x >= distance_y:
                if self.posy >= player_pos[1] : self.moveY('top')
                if self.posy <= player_pos[1] : self.moveY('down')
            else:
                if self.posx >= player_pos[0] : self.moveX('left')
                if self.posx <= player_pos[0] : self.moveX('right')
            self.isRunMove = False
        else:
            self.isRunMove = True

        self.spawn()
        
    def moveX(self, mode):
        if mode == 'left':
            self.posx = self.posx - self.step
            self.posy = self.posy - (self.step / 6)
        if mode == 'right':
            self.posx = self.posx + self.step
            self.posy = self.posy + (self.step / 6)
        
    def moveY(self, mode):
        if mode == 'top':
            self.posy = self.posy - self.step
            self.posx = self.posx - (self.step / 6)
        if mode == 'down':
            self.posy = self.posy + self.step
            self.posx = self.posx + (self.step / 6)
