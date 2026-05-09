import pygame
import sys

pygame.init()

# Window setup
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

# Colours
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Rectangle setup (centered)
rect_width, rect_height = 150, 80
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Font + text
font = pygame.font.SysFont(None, 40)
text_surface = font.render("Hello Pygame!", True, (0, 0, 0))
text_rect = text_surface.get_rect(center=(320, 60))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rect)
    screen.blit(text_surface, text_rect)

    pygame.display.update()
