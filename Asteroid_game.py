# Adopted and adapted PyGame Tutorial from https://coderslegacy.com/python/python-pygame-tutorial/
# Audio files were sourced from the MixKit site under the Mixkit Sound Effects Free License https://mixkit.co/terms/
# Date: 27th March 2023

import sys, pygame, random, time
from pygame.locals import *
 
# Initialising the PyGame engine
pygame.init()
pygame.mixer.init()
 
# Setting frame-per-second (FPS) rate
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Screen information
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SPACE_BACKGROUND = (0, 0, 0)
FONT_COLOUR_SCORE = (255, 255, 255)
FONT_COLOUR_GAMEOVER = (255, 0, 0)
SPEED = 5
SCORE = 0

#Setting up Fonts
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(SPACE_BACKGROUND)
pygame.display.set_caption("Asteroid Hunting")

# Add background music
pygame.mixer.music.load('audio/mixkit-game-level-music-689.wav')
pygame.mixer.music.play()

# Defining Asteroid class 
class Asteroid(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = random.randint(0, 5)
 
      def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed + SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
 
# Defining Earth class
class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Earth.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)

#Setting up Sprites   
asteroid1 = Asteroid()
asteroid2 = Asteroid()
asteroid3 = Asteroid()
asteroid4 = Asteroid()
earth = Earth()

#Creating Sprites Groups
asteroids = pygame.sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
asteroids.add(asteroid4)

all_sprites = pygame.sprite.Group()
all_sprites.add(earth)
all_sprites.add(asteroid1)
all_sprites.add(asteroid2)
all_sprites.add(asteroid3)
all_sprites.add(asteroid4)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while True:     
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(SPACE_BACKGROUND)
    scores = font_small.render(f"Asteroids avoided: {str(SCORE)}", True, FONT_COLOUR_SCORE)
    DISPLAYSURF.blit(scores, (10, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(earth, asteroids):
            pygame.mixer.music.stop()
            pygame.mixer.Sound('audio/mixkit-arcade-chiptune-explosion-1691.wav').play()
            time.sleep(0.5)

            DISPLAYSURF.fill(SPACE_BACKGROUND)
            game_over = font_big.render(f"Game Over! Your score is {SCORE}", True, FONT_COLOUR_GAMEOVER)
            DISPLAYSURF.blit(game_over, (SCREEN_WIDTH / 15, 250))

            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit() 
         
    pygame.display.update()
    FramePerSec.tick(FPS)