"""
Обнавленный алгоритм взаимодейтсвия с игроком:
    Теперь бот должен приблизиться к игроку в опредленный радиус
    после чего вывести свою позицию на ближайшую координату
    затем сделать выстрел и начать снова приследовать игрока, 
    в противном случае, если бот в радиусе действия, надо сделать отступление
"""
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
        print(self.checkRadius(player_pos))
        if self.checkRadius(player_pos):
            self.approximation(player_pos)
        else:
            self.coordinates(player_pos)
                
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

    def checkRadius(self, player_pos):
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

    def coordinates(self, player_pos):
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

    def approximation(self, player_pos):
        vx = player_pos[0] - self.posx
        vy = player_pos[1] - self.posy

        distance = math.sqrt(vx*vx + vy*vy)

        vx /= distance
        vy /= distance

        vx *= self.step
        vy *= self.step

        self.posx += vx
        self.posy += vy
        
