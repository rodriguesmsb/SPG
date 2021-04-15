#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *

## Initialize pygame
pygame.init()

##  Set window dimension
screen_width = 1000
screen_height = 1000

## Create a window
## 

screen = pygame.display.set_mode(size = (screen_width, screen_height))

## Give a title to the window

pygame.display.set_caption("A simple 2d Game")


# load some iamges to drawn on screen

sun_image = pygame.image.load()



## Create the main loop
run = True

while run:
    


    #add a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

