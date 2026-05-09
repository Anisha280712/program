import pygame
import sys

pygame.init()

# Window setup
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Custom Event Demo")

# Define a custom event
MY_EVENT = pygame.USEREVENT + 1

# Trigger the event every 2000 ms (2 seconds)
pygame.time.set_timer(MY_EVENT, 2000)

# Background colour
bg = (200, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle custom event
        if event.type == MY_EVENT:
            print("Custom event triggered!")

    screen.fill(bg)
    pygame.display.update()
