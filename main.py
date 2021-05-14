#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *
from pygame import mixer
from world import World
from player import Player
from button import Button
from word_elements import Coin
import pickle
from os import path


pygame.mixer.pre_init(44100, -16, 2, 512)

#initialize pygame mixer
mixer.init()


## load background sound


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

## Define font
font_score = pygame.font.SysFont("Bauhaus 93", 30)
font_final = pygame.font.SysFont("Bauhaus 93", 70)
font_ghost = pygame.font.SysFont("Bauhaus 93", 70)


## Define game variable
tile_size = 50
game_over = False
main_menu = True
level = 3
max_levels = 7
score = 0

## Define colors
white = (255,255,255)
blue = (0,0,255)
red = "#8b0000"



## load some iamges to drawn on screen

sun = pygame.image.load("img/sun.png")
sky = pygame.image.load("img/sky.png")
dirt = "img/dirt.png"
grass = "img/dirt.png"
restart_image = pygame.image.load("img/restart_btn.png")
start_image = pygame.image.load("img/start_btn.png")
exit_image = pygame.image.load("img/exit_btn.png")


## load background sound
pygame.mixer.music.load("img/music.wav")
pygame.mixer.music.play(-1,0.0,5000)


#define a function to display text
def draw_text(text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    screen.blit(image, (x,y))


#function to reset level
def reset_level(level):
    score_coin = Coin(tile_size //2, tile_size //2, tile_size)
    #create a new world
    #load level data using pickle
    if path.exists("levels/level{}_data".format(level)):
        pickle_in = open("levels/level{}_data".format(level), "rb")
        world_data = pickle.load(pickle_in)

    world = World(data = world_data,  tile_size = tile_size)
    world.coin_group.add(score_coin)
    #reset player
    player.reset(x = 100,
                 y = screen_height - 130, 
                 word_elements = [world.enemey_group, world.lava_group, world.exit_group, world.coin_group, world.platform_group])
    
       
    return world

#Createing a function to display a grid on screen
# def draw_grid():
# 	for line in range(0, 20):
# 		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
# 		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))




## Create world
## world = World(data = world_data,  tile_size = tile_size)
if path.exists("levels/level{}_data".format(level)):
    pickle_in = open("levels/level{}_data".format(level), "rb")
    world_data = pickle.load(pickle_in)

world = World(data = world_data,  tile_size = tile_size)


## Create player
player = Player(x = 100, 
                y = screen_height - 130, 
                word_elements = [world.enemey_group, world.lava_group, world.exit_group, world.coin_group, world.platform_group])


## create menu
restart_button = Button(x = (screen_width // 2) - 10, y = (screen_height // 2) - 100, image = restart_image)
start_button = Button(x = (screen_width // 2) - 350, y = (screen_height // 2), image = start_image)
exit_button =  Button(x = (screen_width // 2) + 150, y = (screen_height // 2), image = exit_image)


## create dummy coin
score_coin = Coin(tile_size //2, tile_size //2, tile_size)
world.coin_group.add(score_coin)

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

        #update score

        #check if the coin was collected
        if pygame.sprite.spritecollide(player, world.coin_group, True):
            score +=1
            player.coin_effect.play()
        draw_text("X " + str(score), font_score, white, tile_size - 10, 15)
        
        world.enemey_group.draw(screen)
        world.lava_group.draw(screen)
        world.exit_group.draw(screen)
        world.coin_group.draw(screen)
        world.platform_group.draw(screen)
        
        
        
        #add move
        world.enemey_group.update()
        world.platform_group.update()

        game_over = player.update_player_position(screen = screen, 
                                    screen_width = screen_width, 
                                    screen_height = screen_height,
                                    world = world,
                                    game_over = game_over)
    
        #if play has die draw restart button
        if game_over == True:
            draw_text("You Died!", font_ghost, red, (screen_width//2) - 140, (screen_height//2))
            if restart_button.draw(screen = screen):
                #restart game again
                player.reset(x = 100, 
                            y = screen_height - 130, 
                            word_elements = [world.enemey_group, world.lava_group, world.exit_group,world.coin_group, world.platform_group])
                game_over = False
                score = 0
        
        #if play passed level
        if game_over == "passed":
            level += 1
            if level <= max_levels:
                #reset lvl
                #clear lvl data
                world_data = []
                world = reset_level(level)
                game_over = False
            else:
                #print a msg tell game end
                draw_text("You Win!", font_final, blue, (screen_width//2) - 140, (screen_height//2))
                #restart lvl
                if restart_button.draw(screen = screen):
                    level = 0
                    world_data = []
                    world = reset_level(level)
                    game_over = False
                    score = 0


    
    #add a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update the screen
    pygame.display.update()

pygame.quit()

