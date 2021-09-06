
import pygame
import math
class Bot_updated:
    def __init__(self, x, y, screen):
        self.posx,self.posy, self.step, self.screen = x, y, 10, screen

        #Uses for calculate method, that stop all calculate
        self.isRun = True
        self.spawn()
    def spawn(self):
        self._self = pygame.Rect(self.posx, self.posy, 20, 20)
        pygame.draw.rect(self.screen, (0,0,255), self._self)
    def calculate(self, player_pos):
        if self.__checkRadius(player_pos):
            self.__approximation(player_pos)
        else:
            self.posx = round(self.posx, -1)
            self.posy = round(self.posy, -1)
            self.__coordinates(player_pos)
                
        self.spawn()      
    def __moveX(self, mode):
        if mode == 'left': self.posx = self.posx - self.step
        if mode == 'right': self.posx = self.posx + self.step
    def __moveY(self, mode):
        if mode == 'top': self.posy = self.posy - self.step
        if mode == 'down': self.posy = self.posy + self.step
    def __checkRadius(self, player_pos):
        #!!!Return not in radius!!!
        radius = 100
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

        if distance_x > distance_y:
            if self.posy > player_pos[1] : self.__moveY('top')
            if self.posy < player_pos[1] : self.__moveY('down')
        else:
            if self.posx > player_pos[0] : self.__moveX('left')
            if self.posx < player_pos[0] : self.__moveX('right')
    def __approximation(self, player_pos):
        vx = player_pos[0] - self.posx
        vy = player_pos[1] - self.posy

        distance = math.sqrt(vx*vx + vy*vy)

        vx /= distance
        vy /= distance

        vx *= self.step
        vy *= self.step

        self.posx += vx
        self.posy += vy
        
