import pygame
import sys

pygame.init()

screen_width = 500
screen_height = 500

blue = (0,0,255)
brown = (244,164,96)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue is the Background with a Brown Rectangle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(blue)


    rectangle_height = 250
    pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))

    pygame.display.flip()

pygame.quit()
sys.exit()


