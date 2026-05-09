import pygame
import sys

pygame.init()

# Window setup
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

# Background colour
grey = (58, 58, 58)

# Load and scale image
image = pygame.image.load("myimage.png")   # put your image in same folder
image = pygame.transform.scale(image, (300, 300))

# Get centre position
image_rect = image.get_rect(center=(250, 250))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(grey)
    screen.blit(image, image_rect)
    pygame.display.update()
