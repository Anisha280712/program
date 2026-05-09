import pygame
import sys

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Pygame Window")

# Background colour
bg = (100, 100, 100)   # soft grey

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)
    pygame.display.update()
