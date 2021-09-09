#Created by: alekseiKromski
import pygame
import sys
import math
from libs.botClass import Bot
from libs.playerClass import Player
import os 
import random
from libs.menuClass import Menu

#Set fps lock
fps = 30
fpsClock = pygame.time.Clock()

ball_init = False

pygame.init()
screen = pygame.display.set_mode((1200, 800))
BIG = pygame.font.Font(os.path.join('fonts','undertale.ttf'), 32)
SMALL = pygame.font.Font(os.path.join('fonts','undertale.ttf'), 16)

#init menu

 
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()        
    if Menu.displayMode == 'menu':
        
        if keys[pygame.K_SPACE]:
            bots = []
            player = Player(screen)
            for i in range(random.randrange(5), random.randrange(15)):
                bot = Bot(random.randrange(0,1200),random.randrange(0,600), screen)
                bots.append(bot)
            displayMenu = False
            screen.blit(Menu.background_menu, (0,0))
            Menu.changeDisplayMode('game')
        
        screen.blit(Menu.background_menu, (0,0))
        screen.blit(Menu.menu, (0,0))
       
    elif Menu.displayMode == 'game':
        player.keys()
        screen.blit(Menu.background, (0,0))
        bots = player.ballActionMethod(bots)
        player.spawn()
        for bot in bots:
            bot.calculate([player.player_X, player.player_Y], bots)

        if len(bots) == 0:
            Menu.changeDisplayMode('point')
    elif Menu.displayMode == 'point':
        
        screen.blit(Menu.point, (0,0))

        
        points = BIG.render("YOUR POINTS : " + str(player.point), True, (240,240,240))
        presstocontinue = SMALL.render("press BACKSPACE to continue ...", True, (240,240,240))
        screen.blit(points, (390, 320))            
        screen.blit(presstocontinue, (380, 420))            
        if keys[pygame.K_BACKSPACE]:
            Menu.changeDisplayMode('menu')
            


    #Execute fps lock
    fpsClock.tick(30)
    pygame.display.update()  

