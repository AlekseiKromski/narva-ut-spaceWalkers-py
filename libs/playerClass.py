import pygame
class Player:
    player_X = 50
    player_Y = 50
    
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
        if keys[pygame.K_RIGHT]:
            self.player_X += 10
        if keys[pygame.K_UP]:
            self.player_Y -= 10   
        if keys[pygame.K_DOWN]:
            self.player_Y += 10 