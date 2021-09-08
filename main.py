#Created by: alekseiKromski
import pygame
import sys
import math
from libs.botClass import Bot
from libs.playerClass import Player
import os 
import random

#Set fps lock
fps = 30
fpsClock = pygame.time.Clock()

ball_init = False

pygame.init()
screen = pygame.display.set_mode((1200, 800))
background = pygame.image.load(os.path.join('textures', 'background.jpg'))

bots = []
player = Player(screen)

for i in range(5):
    bot = Bot(random.randrange(0,1200),random.randrange(0,600), screen)
    bots.append(bot)
 
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    

    player.keys()

    screen.blit(background, (0,0))
    bots = player.ballActionMethod(bots)
        

    player.spawn()

    for bot in bots:
        bot.calculate([player.player_X, player.player_Y], player.view, bots)
    
    #Execute fps lock
    fpsClock.tick(30)
    pygame.display.update()  