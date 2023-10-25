import pygame
import random

from game_parameters import *

def draw_background(screen):
    water = pygame.image.load("../chomp/assets/sprites/water.png").convert()
    sand = pygame.image.load("../chomp/assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../chomp/assets/sprites/seagrass.png").convert()

    #use the png transparency
    water.set_colorkey((0,0,0))
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen with water
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(water, (x, y))


    #draw the sand top along the bottom
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        screen.blit(sand, (x, SCREEN_HEIGHT-TILE_SIZE))

    #distribute seagrass randomly across the sand, not too close to top
    for _ in range(7):
        x = random.randint(0, SCREEN_WIDTH)
        screen.blit(seagrass, (x, SCREEN_HEIGHT-TILE_SIZE*2+20))

    custom_font = pygame.font.Font("../chomp/assets/fonts/Black_Crayon.ttf", 75)

    # create the text "chomp" and display it on the screen
    text = custom_font.render("Chomp", True, (255, 69, 0))

    # draw the text
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 16 - text.get_height() / 16))
