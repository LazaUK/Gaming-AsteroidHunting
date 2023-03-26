# Adopted and adapted PyGame Tutorial from https://coderslegacy.com/python/python-pygame-tutorial/
# Date: 27th March 2023

import sys
import pygame
from pygame.locals import *
import random
 
# Initialising the PyGame engine
pygame.init()
 
# Setting frame-per-second (FPS) rate
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Screen information
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SPACE_BACKGROUND = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(SPACE_BACKGROUND)
pygame.display.set_caption("Asteroid Hunting")

# Defining Asteroid class 
class Asteroid(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = random.randint(5, 10)
 
      def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
# Defining Earth class
class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Earth.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
         
asteroid1 = Asteroid()
asteroid2 = Asteroid()
asteroid3 = Asteroid()
asteroid4 = Asteroid()
earth = Earth()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    earth.update()
    asteroid1.move()
    asteroid2.move()
    asteroid3.move()
    asteroid4.move()
    
    DISPLAYSURF.fill(SPACE_BACKGROUND)
    earth.draw(DISPLAYSURF)
    asteroid1.draw(DISPLAYSURF)
    asteroid2.draw(DISPLAYSURF)
    asteroid3.draw(DISPLAYSURF)
    asteroid4.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)