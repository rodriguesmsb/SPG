#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *
from functions import World

## Initialize pygame
pygame.init()

##  Set window dimension
screen_width = 1000
screen_height = 1000

## Create a window


screen = pygame.display.set_mode(size = (screen_width, screen_height))

## Give a title to the window

pygame.display.set_caption("A simple 2d Game")


## Define game variable
tile_size = 200



## load some iamges to drawn on screen

sun = pygame.image.load("img/sun.png")
sky = pygame.image.load("img/sky.png")
dirt = "img/dirt.png"
grass = "img/dirt.png"

#Createing a function to display a grid on screen
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))




world_data = [
    [1, 1, 1, 1, 1], #first row
    [1, 0, 0, 0, 1], #second row
    [1, 0, 0, 0, 1], #third row
    [1, 0, 0, 0, 1], #fourth row
    [1, 2, 2, 2, 1]
]



## Create dirt path
dirt = World(data = world_data,  tile_size = tile_size)



## Create the main loop
run = True

while run:
    
    #draw the images on the screen
    screen.blit(source = sky, dest = (0,0))
    screen.blit(source = sun, dest = (100,100))

    print(dirt.draw(screen = screen))
    draw_grid()
    

    #add a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update the screen
    pygame.display.update()

pygame.quit()

