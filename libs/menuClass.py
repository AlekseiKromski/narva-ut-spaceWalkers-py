import pygame
import os

'''
This class help game engine control screens menus and game 
'''
class Menu:
    displayMode = 'menu'
    background_menu = pygame.image.load(os.path.join('textures', 'background_menu.jpg'))
    menu = pygame.image.load(os.path.join('textures', 'menu.png'))
    point = pygame.image.load(os.path.join('textures', 'background_point.jpg'))
    background = pygame.image.load(os.path.join('textures', 'background.jpg'))

    @staticmethod
    def changeDisplayMode(mode):
        Menu.displayMode = mode