#Created by: alekseiKromski
import pygame
import sys
import math
from libs.botClass import Bot
from libs.playerClass import Player
import os 


ball_init = False

pygame.init()
screen = pygame.display.set_mode((1200, 800))
background = pygame.image.load(os.path.join('textures', 'background.jpg'))

bots = []
player = Player(screen)
bot1 = Bot(100,200, screen)
bot2 = Bot(800,400, screen)
bots.append(bot1)
bots.append(bot2)

 
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(background, (0,0))

    player.keys()
    if len(bots) != 0:
        bots = player.ballActionMethod(bots)

    player.spawn()

    for bot in bots:
        bot.calculate([player.player_X, player.player_Y], player.view)
    
    pygame.display.update()     