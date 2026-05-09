import pygame
import sys

pygame.init()

# Window setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sprite Movement Demo")

WHITE = (255, 255, 255)

# Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")   # your sprite image
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center=(300, 200))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


player = Player()
all_sprites = pygame.sprite.Group(player)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
