# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:40:06 2025

@author: teres
"""

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants


# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Moving on Random Vectors")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Sprite class
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#        self.image = pygame.Surface((50, 50))  # Create a surface for the sprite
#        self.image.fill(RED)  # Fill it with red color
        SPRITE_FILE = "rock.png"
        SPRITE_SCALE = 4  # Scale factor to make the sprite more visible

        self.image = pygame.image.load(SPRITE_FILE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * SPRITE_SCALE, 16 * SPRITE_SCALE))
        self.rect = self.image.get_rect()  # Get the rectangle (bounding box) of the sprite
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Start at the center of the screen
        
        # Random initial movement vector (dx, dy)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def update(self):
        # Move the sprite by its velocity (dx, dy)
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for collisions with screen edges and reverse direction if needed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx = random.choice([-5, 5])  # New random horizontal velocity
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = random.choice([-5, 5])  # New random vertical velocity

class Scissors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#        self.image = pygame.Surface((50, 50))  # Create a surface for the sprite
#        self.image.fill(RED)  # Fill it with red color
        SPRITE_FILE = "scissors2.png"
        SPRITE_SCALE = 4  # Scale factor to make the sprite more visible

        self.image = pygame.image.load(SPRITE_FILE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * SPRITE_SCALE, 16 * SPRITE_SCALE))
        self.rect = self.image.get_rect()  # Get the rectangle (bounding box) of the sprite
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Start at the center of the screen
        
        # Random initial movement vector (dx, dy)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def update(self):
        # Move the sprite by its velocity (dx, dy)
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for collisions with screen edges and reverse direction if needed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx = random.choice([-5, 5])  # New random horizontal velocity
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = random.choice([-5, 5])  # New random vertical velocity

class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#        self.image = pygame.Surface((50, 50))  # Create a surface for the sprite
#        self.image.fill(RED)  # Fill it with red color
        SPRITE_FILE = "paper.png"
        SPRITE_SCALE = 4  # Scale factor to make the sprite more visible

        self.image = pygame.image.load(SPRITE_FILE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (16 * SPRITE_SCALE, 16 * SPRITE_SCALE))
        self.rect = self.image.get_rect()  # Get the rectangle (bounding box) of the sprite
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Start at the center of the screen
        
        # Random initial movement vector (dx, dy)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def update(self):
        # Move the sprite by its velocity (dx, dy)
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check for collisions with screen edges and reverse direction if needed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx = random.choice([-5, 5])  # New random horizontal velocity
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = random.choice([-5, 5])  # New random vertical velocity


# Create a sprite group and add the sprite
all_sprites = pygame.sprite.Group()
sprite1 = Rock()
sprite2 = Scissors()
sprite3 = Paper()
all_sprites.add(sprite1, sprite2, sprite3)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Check for collision between the two sprites
    if pygame.sprite.collide_rect(sprite1, sprite2):
        # Reverse the direction of both sprites when they collide
        sprite1.dx = random.choice([-5, 5])
        sprite1.dy = random.choice([-5, 5])
        sprite2.dx = random.choice([-5, 5])
        sprite2.dy = random.choice([-5, 5])

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
