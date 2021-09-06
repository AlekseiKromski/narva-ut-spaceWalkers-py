import pygame

class Ball:
    def __init__(self,mode,place, x, y, screen):
       self.posx, self.posy, self.screen, self.step, self.countSteps, self.mode, self.place = x, y, screen, 10, 0, mode, place
       self.isDestroyed = False
    def spawn(self):
        self._self = pygame.Rect(self.posx, self.posy, 20, 20)
        pygame.draw.rect(self.screen, (0,255,0), self._self)
    def strike(self):
        if self.countSteps >= 5:
            self.__destroy()
        else:
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
    def __destroy(self):  
        self.isDestroyed = True
        print('BOM')  

