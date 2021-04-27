#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import pygame
import player


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def draw(self, screen):
        action = False

        #get mouse postion
        pos = pygame.mouse.get_pos()

        #check for mouse hover
        if self.rect.collidepoint(pos):
            
            #0 left, 1 midle, 2 right
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        #check for mouse not benn pressed anymore
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
                
            

        #draw button
        screen.blit(self.image, self.rect)
        return(action)
    




