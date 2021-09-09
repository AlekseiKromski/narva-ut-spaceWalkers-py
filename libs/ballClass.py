from math import radians
import pygame
import os
import sys
from libs.menuClass import Menu
'''
 
'''
class Ball:
    def __init__(self,mode,place, x, y, screen, isBotTexturePack):
       self.posx, self.posy, self.screen, self.step, self.countSteps, self.mode, self.place = x, y, screen, 10, 0, mode, place
       self.isDestroyed = False
       self.textureAnimationCount = 1
       self.isBotTexturePack = isBotTexturePack
       self.image = [
            pygame.image.load(os.path.join('textures', 'shoot_x.png')),
            pygame.image.load(os.path.join('textures', 'shoot_y.png')),
            pygame.image.load(os.path.join('textures', 'shoot_bot_x.png')),
            pygame.image.load(os.path.join('textures', 'shoot_bot_y.png')),
       ]
       self.surf = self.image[0]
    def spawn(self):
        self.screen.blit(self.surf, (self.posx,self.posy))
    def strike(self, bots):
        if self.textureAnimationCount > 1:
            self.__destroy()
        else:
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
                        self.player.point +=1
                        copy_array.pop(i)
                        self.__destroy()
                elif self.mode == 'bottom':
                    if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                        self.player.point +=1
                        copy_array.pop(i)
                        self.__destroy()
                elif self.mode == 'right':
                    if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                        self.player.point +=1
                        copy_array.pop(i)
                        self.__destroy()
                elif self.mode == 'left':
                    if self.posx < c2x and self.posx > c1x and self.posy < c3y and self.posy > c2y:
                        self.player.point +=1
                        copy_array.pop(i)
                        self.__destroy()
                
            if not self.isDestroyed:
                if self.posx == self.place or self.posy == self.place:
                    self.__destroy()
                elif self.textureAnimationCount == 1:
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
        return bots
    def __destroy(self): 
        if self.__bomAnimation():
            self.isDestroyed = True
                
        
    def __setSurfByMode(self, mode):
        if not self.isBotTexturePack:
            if mode == 'left' or mode == 'right':
                self.surf = self.image[0]
            else:
                self.surf = self.image[1]
        else:
            if mode == 'left' or mode == 'right':
                self.surf = self.image[2]
            else:
                self.surf = self.image[3]
    def strikeToPLayer(self, player_pos, view):
        radius = 20
        c1x = player_pos[0] - radius
        c2x = player_pos[0] + radius
        c2y = player_pos[1] - radius
        c3y = player_pos[1] + radius
        self.__setSurfByMode(self.mode)

        if self.mode == 'top':
            if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                Menu.changeDisplayMode('point')
                self.__destroy()
        elif self.mode == 'bottom':
            if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                Menu.changeDisplayMode('point')
                self.__destroy()
        elif self.mode == 'right':
            if self.posx > c1x and self.posx < c2x and self.posy < c3y and self.posy > c2y:
                Menu.changeDisplayMode('point')
                self.__destroy()
                
        elif self.mode == 'left':
            if self.posx < c2x and self.posx > c1x and self.posy < c3y and self.posy > c2y:
                Menu.changeDisplayMode('point')
                self.__destroy() 

        if not self.isDestroyed:
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
        
    def __bomAnimation(self):
        bom_texture = ''
        if self.textureAnimationCount == 1:
            bom_texture = pygame.image.load(os.path.join('textures','bom', '1.png'))
        elif self.textureAnimationCount == 2:
            bom_texture = pygame.image.load(os.path.join('textures','bom', '2.png'))
        elif self.textureAnimationCount == 3:
            bom_texture = pygame.image.load(os.path.join('textures','bom', '3.png'))
            self.screen.blit(bom_texture, (self.posx,self.posy))
            self.textureAnimationCount = 1
            return True

        self.textureAnimationCount += 1
        self.screen.blit(bom_texture, (self.posx,self.posy))
        return False
    def setPlayerInstance(self, player):
        self.player = player