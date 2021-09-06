#Created by: alekseiKromski
import pygame
import sys
import math
from libs.botClassBeta import Bot_updated
from libs.playerClass import Player

pygame.init()
screen = pygame.display.set_mode((1200, 800))

player = Player(screen)
bot1_beta = Bot_updated(900,350, screen)

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((0, 0, 0))

    player.keys()
    player.spawn()
    bot1_beta.calculate([player.player_X, player.player_Y])
    
    pygame.display.update()     