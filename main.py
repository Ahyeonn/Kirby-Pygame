# Import and initialize pygame
from random import randint, choice
import pygame
from black import Black
from GameObject import GameObject
from kirby import Kirby
from red import Red
from yellow import Yellow
from green import Green
from constants import lanes, background, screen
from ScoreBoard import ScoreBoard

pygame.init()
pygame.font.init()

# Make an instance of GameObject
red = Red()
red2 = Red()
red3 = Red()
yellow = Yellow()
yellow2 = Yellow()
yellow3 = Yellow()
green = Green()
green2 = Green()
green3 = Green()
kirby = Kirby()
black = Black()
black2 = Black()
black3 = Black()
score = ScoreBoard(25, 25, 0)
all_sprites = pygame.sprite.Group()
red_sprites = pygame.sprite.Group()
green_sprites = pygame.sprite.Group()
yellow_sprites = pygame.sprite.Group()
all_sprites.add(score)


# Add sprites to group
all_sprites.add(kirby)
all_sprites.add(red)
all_sprites.add(red2)
all_sprites.add(red3)
all_sprites.add(green)
all_sprites.add(green2)
all_sprites.add(green3)
all_sprites.add(yellow)
all_sprites.add(yellow2)
all_sprites.add(yellow3)
all_sprites.add(black)
all_sprites.add(black2)
all_sprites.add(black3)
red_sprites.add(red)
red_sprites.add(red2)
red_sprites.add(red3)
green_sprites.add(green)
green_sprites.add(green2)
green_sprites.add(green3)
yellow_sprites.add(yellow)
yellow_sprites.add(yellow2)
yellow_sprites.add(yellow3)

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Check for event type KEYBOARD
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        kirby.left()
      elif event.key == pygame.K_RIGHT:
        kirby.right()
      elif event.key == pygame.K_UP:
        kirby.up()
      elif event.key == pygame.K_DOWN:
        kirby.down()

  # Draw a circle
  screen.fill((223, 161, 143))
  screen.blit(background, (0, 0))
  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
  
  # Check Colisions
  red = pygame.sprite.spritecollideany(kirby, red_sprites)
  if red:
    score.update(50)
    red.reset()
  
  yellow = pygame.sprite.spritecollideany(kirby, yellow_sprites)
  if yellow:
    score.update(10)
    yellow.reset()
  
  green = pygame.sprite.spritecollideany(kirby, green_sprites)
  if green:
    score.update(100)
    green.reset()
  
  # Check collision player and bomb
  if pygame.sprite.collide_rect(kirby, black):
    running = False
  elif pygame.sprite.collide_rect(kirby, black2):
    running = False
  elif pygame.sprite.collide_rect(kirby, black3):
    running = False
  # Update the window
  pygame.display.flip()



