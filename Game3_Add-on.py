import pygame
import sys
import random

#imitialize Pygame
pygame.init()

#screen dimensions
tile_size = 64
screen_width = 800
screen_height = 600

#create a screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

#main loop
running = True
background = screen.copy()

#load tiles from the assets folder into surfaces
water = pygame.image.load("../chomp/assets/sprites/water.png").convert()
sand = pygame.image.load("../chomp/assets/sprites/sand_top.png").convert()
seagrass = pygame.image.load("../chomp/assets/sprites/seagrass.png").convert()

#use the png transparency
water.set_colorkey((0,0,0))
sand.set_colorkey((0,0,0))
seagrass.set_colorkey((0,0,0))

#fill the screen with water
for x in range(0, screen_width, tile_size):
    for y in range(0, screen_height, tile_size):
        background.blit(water, (x, y))


#draw the sand top along the bottom
for x in range(0, screen_width, tile_size):
    background.blit(sand, (x, screen_height-tile_size))

#distribute seagrass randomly across the sand, not too close to top
for _ in range(7):
    x = random.randint(0, screen_width)
    background.blit(seagrass, (x, screen_height-tile_size*2+20))

#load game font
custom_font = pygame.font.Font("../chomp/assets/fonts/From_Cartoon_Blocks.ttf", 100)

#create the text "chomp" and display it on the screen
text = custom_font.render("Joe Van Dyk", True, (48, 130, 0))

#main code
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the background
    screen.blit(background, (0,0))

    #draw the text
    screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))
    #drawing the text on the top half middle of the screen
    #screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/4 - text.get_height()/4))
    #drawing the text on the bottom half middle of the screen
    #screen.blit(text, (screen_width/2 - text.get_width()/2, 3*screen_height/4 - 3*text.get_height()/4))

    #update the display
    pygame.display.flip()

pygame.quit()
sys.exit()