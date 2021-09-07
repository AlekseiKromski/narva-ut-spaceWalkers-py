
import pygame
import math
import os

from pygame import image
class Bot:
    def __init__(self, x, y, screen):
        self.posx,self.posy, self.step, self.screen = x, y, 10, screen
        self.color = (0,0,255)
        self.tick = 0
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
    def calculate(self, player_pos, player_view):
        if self.__checkRadius(player_pos):
            self.__approximation(player_pos)
        else:
            self.posx = round(self.posx, -1)
            self.posy = round(self.posy, -1)
            self.__coordinates(player_pos)
            self.tick += 1
            self.__defineTextureInCoorfinate(player_view)  

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
    def __defineTextureInCoorfinate(self, mode):
        if mode == "right":
            self.__setSurf(self.image[3][0])
        elif mode == "left":
            self.__setSurf(self.image[1][0])
        elif mode == "bottom":
            self.__setSurf(self.image[2][0])
        elif mode == "top":
            self.__setSurf(self.image[0][0])