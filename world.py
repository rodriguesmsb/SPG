#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import pygame
from enemey import Enemey


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