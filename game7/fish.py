import pygame
import random

MIN_SPEED = .5
MAX_SPEED = 3


#sublcassing the Sprite by calling the base initializer before adding the Sprite to Groups
class Fish(pygame.sprite.Sprite):
    #constructor. Pass in its x and y position and/or the color and dimensions of the block
    def __init__(self, x, y):
        #inherit from the parent class (Sprite)
        super().__init__()

        #load an image from the disk. You can also create a surface with the pygame.Surface((w,h))
        self.image = pygame.image.load("../game7/assets/sprites/green_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)
        #set the transparency values
        self.image.set_colorkey((0,0,0))

        #fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        #update the position of the object by setting the values of rect.x and rect.y
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    #update object position
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()