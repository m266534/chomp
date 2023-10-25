import pygame
import sys
import random
from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish

#imitialize Pygame
pygame.init()


#create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

chomp = pygame.mixer.Sound("../game6/assets/sounds/chomp.wav")
clock = pygame.time.Clock()


for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2),random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))



running = True
background = screen.copy()
draw_background(background)

add_fish(5)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

score = 0
score_font = pygame.font.Font("../game6/assets/fonts/Black_Crayon.ttf", 48)
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


    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        score += len(result)

        pygame.mixer.Sound.play(chomp)

        add_fish(len(result))

    #get rid of fish that move off the screen and add new fish
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            # fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE*2, random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
            add_fish(1)
    #draw game objects
    fishes.draw(screen)
    player.draw(screen)


    text = score_font.render(f"{score}", True, (255,69,0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))
    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()