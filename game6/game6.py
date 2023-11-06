import pygame
import sys
import random
from fish import Fish, fishes
from player import Player
from game_parameters import *
from utilities import draw_background, add_fish
import pygame.mixer
#imitialize Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("../game6/assets/sounds/Jaws.mp3")
pygame.mixer.music.play(-1)

#create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using blit to draw tiles")

font = pygame.font.Font(None, 36)
chomp = pygame.mixer.Sound("../game6/assets/sounds/chomp.wav")
clock = pygame.time.Clock()

welcome_font = pygame.font.Font("../game6/assets/fonts/Black_Crayon.ttf", 75)
welcome_text = welcome_font.render("Welcome to Chomp!", True, (255, 69, 0))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
welcome_timer = 3 * 60

game_over_timer = 120 * 60
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2),random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))



running = True
background = screen.copy()
draw_background(background)

add_fish(5)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

score = 0
score_font = pygame.font.Font("../game6/assets/fonts/Black_Crayon.ttf", 48)
game_won = False
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

    if welcome_timer > 0:
        screen.blit(background, (0,0))
        screen.blit(welcome_text, welcome_rect)
        pygame.display.flip()
        welcome_timer -= 1

    else:

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

        if score >= 20:
            game_won = True

        if game_over_timer <= 0 or game_won:
            game_over_text = None

            if game_won:
                game_over_text = score_font.render(f"You Win!", True, (0, 255, 0))
            else:
                game_over_text = score_font.render(f"You lose :(", True, (0, 255, 0))

            game_over_rect = game_over_text.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(game_over_text, game_over_rect)
            pygame.display.flip()

            pygame.time.wait(2000)
            running = False
    #update the display
        pygame.display.flip()

    #limit the frame rate
    clock.tick(60)
    game_over_timer -= 1

pygame.quit()
sys.exit()