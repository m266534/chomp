import pygame
import sys
import random
from fish import Fish, fishes
from fish_2 import Fish_2, fishes_more
#imitialize Pygame
pygame.init()

#screen dimensions
tile_size = 64
screen_width = 800
screen_height = 600

#create a screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

clock = pygame.time.Clock()
#main loop
running = True
background = screen.copy()

#load tiles from the assets folder into surfaces
def draw_background(screen):
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
            screen.blit(water, (x, y))


    #draw the sand top along the bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height-tile_size))

    #distribute seagrass randomly across the sand, not too close to top
    for _ in range(7):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height-tile_size*2+20))

    custom_font = pygame.font.Font("../chomp/assets/fonts/Black_Crayon.ttf", 75)

    # create the text "chomp" and display it on the screen
    text = custom_font.render("Chomp", True, (255, 69, 0))

    # draw the text
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 16 - text.get_height() / 16))

background = screen.copy()
draw_background(background)
    #load game font


for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2),random.randint(tile_size, screen_height - tile_size)))
for __ in range(5):
    fishes_more.add(Fish_2(random.randint(-screen_width, 0), random.randint(tile_size, screen_height - tile_size)))


#main code
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #draw the background
    screen.blit(background, (0,0))

    #update game objects
    fishes.update()
    fishes_more.update()

    #get rid of fish that move off the screen and add new fish
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(screen_width, random.randint(tile_size, screen_height - tile_size)))

    # for fish_2 in fishes_more:
    #     if fish_2.rect.x > fish_2.rect.width * 2:
    #         fishes_more.remove(fish_2)
    #         fishes_more.add(Fish_2(0, random.randint(tile_size, screen_height - tile_size)))
    #draw game objects
    fishes.draw(screen)
    fishes_more.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
