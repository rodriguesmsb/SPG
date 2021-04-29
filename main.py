#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *
from world import World
from player import Player
from button import Button
import pickle


## Initialize pygame
pygame.init()

## add frame rate to game
clock = pygame.time.Clock()
fps = 60


##  Set window dimension
screen_width = 1000
screen_height = 1000

## Create a window
screen = pygame.display.set_mode(size = (screen_width, screen_height))

## Give a title to the window

pygame.display.set_caption("A simple 2d Game")


## Define game variable
tile_size = 50
game_over = False
main_menu = True
level = 8



## load some iamges to drawn on screen

sun = pygame.image.load("img/sun.png")
sky = pygame.image.load("img/sky.png")
dirt = "img/dirt.png"
grass = "img/dirt.png"
restart_image = pygame.image.load("img/restart_btn.png")
start_image = pygame.image.load("img/start_btn.png")
exit_image = pygame.image.load("img/exit_btn.png")


#Createing a function to display a grid on screen
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))



#load level data using pickle
try:
    pickle_in = open("levels/level{}_data".format(level), "rb")
    world_data = pickle.load(pickle_in)
except:
    pickle_in = open("levels/level1_data".format(level), "rb")
    world_data = pickle.load(pickle_in)


## Create world
world = World(data = world_data,  tile_size = tile_size)

## Create player
player = Player(x = 100, y = screen_height - 130, enemies_list = [world.enemey_group, world.lava_group, world.exit_group])

## create menu
restart_button = Button(x = (screen_width // 2) - 10, y = (screen_height // 2) - 100, image = restart_image)
start_button = Button(x = (screen_width // 2) - 350, y = (screen_height // 2), image = start_image)
exit_button =  Button(x = (screen_width // 2) + 150, y = (screen_height // 2), image = exit_image)


## Create the main loop
run = True

while run:


    #limit the pc to run the game a specific fps
    clock.tick(fps)
  
    #draw the images on the screen
    screen.blit(source = sky, dest = (0,0))
    screen.blit(source = sun, dest = (100,100))


    if main_menu == True:
        #load menu before draw world
        if exit_button.draw(screen = screen):
            run = False
        if start_button.draw(screen = screen):
            main_menu = False


    else:
        world.draw(screen = screen)
        world.enemey_group.draw(screen)
        world.lava_group.draw(screen)
        world.exit_group.draw(screen)
        #add move
        world.enemey_group.update()
        game_over = player.update_player_position(screen = screen, 
                                    screen_width = screen_width, 
                                    screen_height = screen_height,
                                    world = world,
                                    game_over = game_over)
    
        #if play die draw restart button
        if game_over == True:
            if restart_button.draw(screen = screen):
                #restart game again
                player.reset(x = 100, 
                            y = screen_height - 130, 
                            enemies_list = [world.enemey_group, world.lava_group])
                game_over = False

    
        
    #add a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update the screen
    pygame.display.update()

pygame.quit()

