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
        radius = 75
        self.__setSurfByMode(self.mode)
        copy_array = []
        for bot in bots:
            copy_array.append(bot)

        for i in range(len(bots)):
            if self.mode == 'top':
                if self.posx == bots[i].posx and self.posy > bots[i].posy - radius and self.posy < bots[i].posy + radius:
                    copy_array.pop(i)
                    self.__destroy()
            elif self.mode == 'bottom':
                if self.posx == bots[i].posx and self.posy > bots[i].posy - radius and self.posy < bots[i].posy + radius:
                    copy_array.pop(i)
                    self.__destroy()  
            elif self.mode == 'right':
                if self.posy == bots[i].posy and self.posx > bots[i].posx - radius and self.posx < bots[i].posx + radius:
                    copy_array.pop(i)
                    self.__destroy()
                    
            elif self.mode == 'left':
                if self.posy == bots[i].posy and self.posx > bots[i].posx - radius and self.posx < bots[i].posx + radius:
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
        print('BOM')  
    def __setSurfByMode(self, mode):
        if mode == 'left' or mode == 'right':
            self.surf = self.image[0]
        else:
            self.surf = self.image[1]


