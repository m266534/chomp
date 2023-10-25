import pygame
import sys
import random
from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background

#imitialize Pygame
pygame.init()


#create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

clock = pygame.time.Clock()

background = screen.copy()
draw_background(background)


for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2),random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))


player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
running = True
#main code
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #control player
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key ==pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key ==pygame.K_RIGHT:
                player.move_right()

        #draw the background
    screen.blit(background, (0,0))

    #update game objects
    fishes.update()
    player.update()

    #get rid of fish that move off the screen and add new fish
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE*2, random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
    #draw game objects
    fishes.draw(screen)
    player.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
