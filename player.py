import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    #constructor. Pass in its x and y position and/or the color and dimensions of the block
    def __init__(self, x, y):
        #inherit from the parent class (Sprite)
        super().__init__()

        #load an image from the disk. You can also create a surface with the pygame.Surface((w,h))
        self.foward_image = pygame.image.load("../chomp/assets/sprites/orange_fish.png").convert()
        # set the transparency values
        self.foward_image.set_colorkey((0, 0, 0))
        size = self.foward_image.get_size()
        newsize = (size[0] * 1.5, size[1] * 1.5)
        self.foward_image = pygame.transform.scale(self.foward_image, newsize)
        self.reverse_image = pygame.transform.scale(self.foward_image, newsize)
        self.reverse_image = pygame.transform.flip(self.foward_image, True, False)
        self.upwards_image = pygame.transform.scale(self.foward_image, newsize)
        self.upwards_image = pygame.transform.rotate(self.foward_image, 90)
        self.downward_image = pygame.transform.scale(self.foward_image, newsize)
        self.downward_image = pygame.transform.rotate(self.foward_image, 270)



        #fetch the rectangle object that has the dimensions of the image
        self.image = self.foward_image
        self.rect = self.image.get_rect()
        #update the position of the object by setting the values of rect.x and rect.y
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_velocity = 0
        self.y_velocity = 0

    def move_up(self):
        self.y_velocity = - PLAYER_SPEED
        self.image = self.upwards_image

    def move_down(self):
        self.y_velocity = PLAYER_SPEED
        self.image = self.downward_image

    def move_left(self):
        self.x_velocity = -1 * PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        self.image = self.foward_image

    def stop(self):
        self.y_velocity = 0
        self.x_velocity = 0

    #update object position
    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()