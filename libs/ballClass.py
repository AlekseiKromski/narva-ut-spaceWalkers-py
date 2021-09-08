from math import radians
import pygame
import os
'''
 
'''
class Ball:
    def __init__(self,mode,place, x, y, screen):
       self.posx, self.posy, self.screen, self.step, self.countSteps, self.mode, self.place = x, y, screen, 10, 0, mode, place
       self.isDestroyed = False
       self.image = [
            pygame.image.load(os.path.join('textures', 'shoot_x.png')),
            pygame.image.load(os.path.join('textures', 'shoot_y.png'))
       ]
       self.surf = self.image[0]
    def spawn(self):
        self.screen.blit(self.surf, (self.posx,self.posy))
    def strike(self, bots):
        radius = 20
        self.__setSurfByMode(self.mode)
        
        copy_array = []
        for bot in bots:
            copy_array.append(bot)

        for i in range(len(bots)):
            c1x = bots[i].posx - radius
            c2x = bots[i].posx + radius
            c2y = bots[i].posy - radius
            c3y = bots[i].posy + radius

            if self.mode == 'top':
                if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                    copy_array.pop(i)
                    self.__destroy()
            elif self.mode == 'bottom':
                if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                    copy_array.pop(i)
                    self.__destroy()
            elif self.mode == 'right':
                if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                    copy_array.pop(i)
                    self.__destroy()
                    
            elif self.mode == 'left':
                if self.posx < c2x and self.posx > c1x and self.posy < c3y and self.posy > c2y:
                    copy_array.pop(i)
                    self.__destroy()
            

        if self.countSteps >= 5:
            self.__destroy()
        elif not self.isDestroyed:
            if self.posx == self.place or self.posy == self.place:
                self.__destroy()
            else:
                if self.mode == 'left':
                    self.posx -= self.step
                elif self.mode == 'right':
                    self.posx += self.step
                elif self.mode == 'top':
                    self.posy -= self.step
                elif self.mode == 'bottom':
                    self.posy += self.step
                
                self.spawn()
        return copy_array
    def __destroy(self):  
        self.isDestroyed = True
         
    def __setSurfByMode(self, mode):
        if mode == 'left' or mode == 'right':
            self.surf = self.image[0]
        else:
            self.surf = self.image[1]
    def strikeToPLayer(self, player_pos, view):
        self.__setSurfByMode(self.mode)
        if self.mode == 'left':
            self.posx -= self.step
        elif self.mode == 'right':
            self.posx += self.step
        elif self.mode == 'top':
            self.posy -= self.step
        elif self.mode == 'bottom':
            self.posy += self.step

        if not self.isDestroyed:
            print(self.place)
            print(self.posx)
            if self.posx == self.place or self.posy == self.place:
                print('BOM') 
                self.__destroy()
            else:
                if self.mode == 'left':
                    self.posx -= self.step
                elif self.mode == 'right':
                    self.posx += self.step
                elif self.mode == 'top':
                    self.posy -= self.step
                elif self.mode == 'bottom':
                    self.posy += self.step
                
                self.spawn()
