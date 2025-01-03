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
class rps(pygame.sprite.Sprite):
    def __init__(self, rps_type):
        super().__init__()

        ROCK_FILE = "rock.png"
        PAPER_FILE = "paper.png"
        SCISSORS_FILE = "scissors.png"
        SPRITE_SCALE = 2  # Scale factor to make the sprite more visible
        
        if rps_type == 'rock':
            self.image = pygame.image.load(ROCK_FILE).convert_alpha()
        elif rps_type == 'paper':
            self.image = pygame.image.load(PAPER_FILE).convert_alpha()
        else:
            self.image = pygame.image.load(SCISSORS_FILE).convert_alpha()
            
            
        self.image = pygame.transform.scale(self.image, (16 * SPRITE_SCALE, 16 * SPRITE_SCALE))
        self.rect = self.image.get_rect()  # Get the rectangle (bounding box) of the sprite
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Start at the center of the screen
        
        # Random initial movement vector (dx, dy)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def reimage(self):
        
        self.image = pygame.image.load("paper.png").convert_alpha()
        
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
sprite1 = rps('rock')
sprite2 = rps('paper')
all_sprites.add(sprite1, sprite2)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
        
    # Update all sprites
    all_sprites.update()
    
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
