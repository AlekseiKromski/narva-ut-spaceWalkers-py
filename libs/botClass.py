
import pygame
import math
import os
from libs.ballClass import Ball
import uuid
from pygame import image
import random
class Bot:
    def __init__(self, x, y, screen):
        self.posx,self.posy, self.step, self.screen = x, y, 10, screen
        self.color = (0,0,255)
        self.tick = 0
        self.shot = True
        self.ballInit = False
        self.shotDistance = 150
        self.definePlayerSideForStrike = None
        self.id = uuid.uuid1()
        self.fly_mode = 'normal'
        self.randomCoordinates = None
        self.toCoordinateTimer = 0
        self.image = [
        [os.path.join('textures', 'bot', 'bot_top.png')],
        [os.path.join('textures', 'bot', 'bot_right.png')],
        [os.path.join('textures', 'bot', 'bot_bottom.png')],
        [os.path.join('textures', 'bot', 'bot_left.png')],

        [os.path.join('textures', 'bot', 'bot_top_left.png')],
        [os.path.join('textures', 'bot', 'bot_top_right.png')],
        [os.path.join('textures', 'bot', 'bot_bottom_left.png')],
        [os.path.join('textures', 'bot', 'bot_bottom_right.png')],
        ]

        self.surf = pygame.image.load(self.image[1][0])

        #Uses for calculate method, that stop all calculate
        self.isRun = True
        self.spawn()
    def spawn(self):
        self.screen.blit(self.surf, (self.posx,self.posy))
    def calculate(self, player_pos, bots):
        
        if self.fly_mode == 'normal':
            
            self.__findBotsInRadius(bots)
            #Change state
            self.randomCoordinates = None
            #Change state
            self.toCoordinateTimer = 0

            if self.__checkRadius(player_pos):
                self.__approximation(player_pos)
            else:
                self.posx = round(self.posx, -1)
                self.posy = round(self.posy, -1)
                self.__coordinates(player_pos)
                self.tick += 1
                self.__defineTextureByPlayer(player_pos)   
        elif self.fly_mode == 'tocoordinates':
            if self.randomCoordinates == None:
                self.randomCoordinates = [random.randrange(0, 1200), random.randrange(0, 600)]
                self.toCoordinateTimer = 0
            if self.toCoordinateTimer < 15:
                self.__approximation(self.randomCoordinates)
                self.toCoordinateTimer += 1
            if self.toCoordinateTimer >= 15:
                self.fly_mode = 'normal'
        

        self.__initStrike(player_pos) 

        self.spawn()      
    def __moveX(self, mode):
        if mode == 'left': self.posx = self.posx - self.step
        if mode == 'right': self.posx = self.posx + self.step
    def __moveY(self, mode):
        if mode == 'top': self.posy = self.posy - self.step
        if mode == 'down': self.posy = self.posy + self.step
    def __checkRadius(self, player_pos):
        #!!!Return not in radius!!!
        radius = 150
        player_pox_x_with_radius_right = player_pos[0] + radius
        player_pox_x_with_radius_left = player_pos[0] - radius

        player_pox_y_with_radius_bottom = player_pos[1] + radius
        player_pox_y_with_radius_top = player_pos[1] - radius
        if(
            self.posx > player_pox_x_with_radius_right or
            self.posx < player_pox_x_with_radius_left or
            self.posy < player_pox_y_with_radius_top or
            self.posy > player_pox_y_with_radius_bottom
        ):
            return True
        else:
            return False
    def __coordinates(self, player_pos):
        radius = 10
        #Find y distance
        distance_y = math.fabs(self.posy - player_pos[1])

        #Find x distance
        distance_x = math.fabs(self.posx - player_pos[0])

        if distance_x > distance_y and self.tick == 2:
            if self.posy > player_pos[1] : self.__moveY('top')
            if self.posy < player_pos[1] : self.__moveY('down')
            self.tick = 0

        elif distance_x < distance_y and self.tick == 2:
            if self.posx > player_pos[0] : self.__moveX('left')
            if self.posx < player_pos[0] : self.__moveX('right')
            self.tick = 0
        
        #Strike
    def __approximation(self, player_pos):
        vx = player_pos[0] - self.posx
        vy = player_pos[1] - self.posy

        distance = math.sqrt(vx*vx + vy*vy)

        vx /= distance
        vy /= distance

        
        vx *= self.step
        vy *= self.step

        self.__defineTextureInapproximation(vx, vy)

        self.posx += vx
        self.posy += vy
    def __delete__(self):
        self.color = (0,0,0)
        del self
    def __defineTextureInapproximation(self, x, y):
        if x < 0 and y < 0:
            self.__setSurf(self.image[4][0])
        elif x < 0 and y > 0:
            self.__setSurf(self.image[6][0])
        elif x > 0 and y > 0:
            self.__setSurf(self.image[7][0])
        elif x > 0 and y < 0:
            self.__setSurf(self.image[5][0])  
    def __setSurf(self, img):
        self.surf = pygame.image.load(img)
    def __defineTextureByPlayer(self, player_pos):

        if player_pos[0] > self.posx:
            self.__setSurf(self.image[1][0])
        elif player_pos[0] < self.posx:
            self.__setSurf(self.image[3][0])


        if player_pos[1] > self.posy:
            self.__setSurf(self.image[2][0])
        elif player_pos[1] < self.posy:
            self.__setSurf(self.image[0][0])
    def __strike(self, player_pos, to):
        if self.ball.isDestroyed:
            self.shot = True
        else:
            self.ball.strikeToPLayer(player_pos, to)   
    def __initBall(self, to):
        if to == 'right':
            self.ball = Ball(to, self.posx + self.shotDistance, self.posx, self.posy, self.screen, True)
        if to == 'left':
            self.ball = Ball(to, self.posx - self.shotDistance, self.posx, self.posy, self.screen, True)
        if to == 'bottom':
            self.ball = Ball(to, self.posy + self.shotDistance, self.posx, self.posy, self.screen, True)
        if to == 'top':
            self.ball = Ball(to, self.posy - self.shotDistance, self.posx, self.posy, self.screen, True)
    def __findBotsInRadius(self, bots):
        radius = 100
        for i in range(len(bots)):
            c1x = bots[i].posx - radius
            c2x = bots[i].posx + radius
            c2y = bots[i].posy - radius
            c3y = bots[i].posy + radius

            if self.id != bots[i].id:
                if self.posx > c1x and self.posx < c2x and self.posy > c2y and self.posy < c3y:
                    self.fly_mode = 'tocoordinates'
    def __setNewBall(self):
        if self.definePlayerSideForStrike != None:
                self.shot = False
                self.__initBall(self.definePlayerSideForStrike)
    def __initStrike(self, player_pos):
        radius = 20 
        #Init strike
        if self.shot:
            if self.posy > player_pos[1] - radius and self.posy < player_pos[1] + radius:
                if player_pos[0] < self.posx :
                    self.definePlayerSideForStrike = 'left'
                else:
                    self.definePlayerSideForStrike = 'right'
                self.__setNewBall()
            elif self.posx > player_pos[0] - radius and self.posx < player_pos[0] + radius:
                if player_pos[1] < self.posy:
                    self.definePlayerSideForStrike = 'top'
                else:
                    self.definePlayerSideForStrike = 'bottom'
                self.__setNewBall()
        else:
            
            self.__strike(player_pos, self.definePlayerSideForStrike)