import pygame
import sys
import random

import pygame.mouse

from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish, add_enemies
from enemy import Enemy, enemies

#imitialize Pygame
pygame.init()


#create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

chomp = pygame.mixer.Sound("C:/Users/m266534/Documents/EW200/Labs/chomp/game7/assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../game7/assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../game7/assets/sounds/bubbles.wav")
life_icon = pygame.image.load("../game7/assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0,0,0))
clock = pygame.time.Clock()


for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2),random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))



running = True
background = screen.copy()
draw_background(background)

add_fish(5)
add_enemies(3)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../game7/assets/fonts/Black_Crayon.ttf", 48)
while lives > 0:
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_x, click_y = event.pos
                player.rect.center = (click_x, click_y)


    #update game objects
    fishes.update()
    enemies.update()
    player.update()


    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        score += len(result)

        pygame.mixer.Sound.play(chomp)

        add_fish(len(result))

    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)

        pygame.mixer.Sound.play(hurt)

        add_enemies(len(result))

    #get rid of fish that move off the screen and add new fish
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            # fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE*2, random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))
            add_fish(1)

    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)

    #draw the background
    screen.blit(background, (0,0))

    #draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)


    text = score_font.render(f"{score}", True, (255,69,0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

screen.blit(background, (0,0))
message = score_font.render("Game Over", True, (0,0,0))
screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2, SCREEN_HEIGHT / 2 - message.get_height() / 2))

score_text = score_font.render(f"Score: {score}", True, (0,0,0))
screen.blit(score_text, (SCREEN_WIDTH / 2 -score_text.get_width() / 2, SCREEN_HEIGHT /2 + message.get_height()))

pygame.display.flip()

pygame.mixer.Sound.play(bubbles)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# pygame.quit()
# sys.exit()