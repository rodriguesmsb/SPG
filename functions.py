#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import pygame

class World():
    def __init__(self, data, tile_size):

        self.tile_list = []
        self.enemey_group = pygame.sprite.Group()

        dirt = pygame.image.load("img/dirt.png")
        grass = pygame.image.load("img/grass.png")

        tile_size = tile_size

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt,(tile_size, tile_size))

                    #Create a rectangle with the size of image
                    img_rect = img.get_rect()

                    #increase coordinates according to position on data
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(grass,(tile_size, tile_size))
                    #Create a rectangle with the size of image
                    img_rect = img.get_rect()
                    #increase coordinates according to position on data
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemey(x = col_count * tile_size, y = row_count * tile_size + 15)
                    self.enemey_group.add(blob)
                col_count += 1
            row_count += 1
    
    #draw images
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

            #Add a rectangle at each img
            pygame.draw.rect(screen, (255,255,255), tile[1], 2)


#create enemey class
#this class will be a child of pygame.sprite.Sprite)
#pygame.sprite already have a draw and update method
class Enemey(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/blob.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
    
    def update(self):
        
        self.rect.x += self.move_direction

        #check for collision
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

        




class Player():
    def __init__(self, x, y):

        #create a blank list
        self.images_right = []
        self.images_left = []

        #track list index
        self.index = 0
        self.counter = 0

        #load the images
        for num in range(1,5):
            img_path = "img/guy" + str(num) + ".png"
            img_right = pygame.image.load(img_path)

            player_right = pygame.transform.scale(img_right,(40,80))

            #flip image 
            player_left = pygame.transform.flip(player_right, True, False)

            self.images_right.append(player_right)
            self.images_left.append(player_left)
        
        #get images from list to display on screen
        self.player = self.images_right[self.index]
        self.player_rect = self.player.get_rect()

        #get player position
        self.player_rect.x = x
        self.player_rect.y = y
        self.width = self.player.get_width()
        self.height = self.player.get_height()
        self.player_jump_vel = 0
        self.player_jumped = False
        self.direction = "right"
    
    def update_player_position(self, screen, screen_width, screen_height, world):

        # we need 3 steps to update position in this game
        # 1 calculate player position
        # 2 check collision at new positon
        # 3 adjust player position

        dx = 0
        dy = 0
        walk_speed  = 5

        #get key press
        key = pygame.key.get_pressed()

        #Add left move
        if key[pygame.K_LEFT]:
            dx -= 5
            self.direction = "left"

        if key[pygame.K_RIGHT]:
            #change character position
            dx += 5
            self.direction = "right"




        #add jump evevent
        if key[pygame.K_SPACE] and self.player_jumped == False:
            self.player_jump_vel = -15
            self.player_jumped = True

        #stopping jum event
        if key[pygame.K_SPACE] == False:
            self.player_jumped = False


        #block code to handle with animation

        #add code to star animation only if key is pressed
        if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
            self.counter += 1
        
       
        #Add animation during the move
        if self.counter > walk_speed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == "right":
                self.player = self.images_right[self.index]
            if self.direction == "left":
                self.player = self.images_left[self.index]

        
         #add guy to stop position
        if key[pygame.K_RIGHT] == False and key[pygame.K_LEFT] == False:
            self.counter = 0
            if self.direction == "right":
                self.player = self.images_right[0]
            if self.direction == "left":
                self.player = self.images_left[0]
        
       

        ## add gravity
        self.player_jump_vel += 1
        if self.player_jump_vel > 10:
            self.player_jump_vel = 10
        dy += self.player_jump_vel

    
        
        #check for collision
        for tile in world.tile_list:
            #check for x collision
            if tile[1].colliderect(self.player_rect.x + dx, self.player_rect.y, self.width, self.height):
                dx = 0
            #check for collision on y direction
            if tile[1].colliderect(self.player_rect.x, self.player_rect.y + dy, self.width, self.height):
                #check if the player is bellow the ground i.e jumping
                if self.player_jump_vel < 0:
                    dy = tile[1].bottom - self.player_rect.top
                    self.player_jump_vel = 0

                #check if the player is above the ground i.e falling
                elif self.player_jump_vel > 0:
                    dy = tile[1].top - self.player_rect.bottom
            
            


            
        #update player coordinate
        self.player_rect.x += dx
        self.player_rect.y += dy


        #Check if the player move away from screen
        if self.player_rect.bottom > screen_height:
            self.player_rect.bottom = screen_height
            dy = 0


        #draw player on screen
        screen.blit(self.player, self.player_rect)

        #draw a rect around char
        pygame.draw.rect(screen, (255,255,255), self.player_rect, 2)
       

    


         
