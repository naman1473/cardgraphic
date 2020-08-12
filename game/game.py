import pygame
import os

# Game scene size
window = pygame.display.set_mode((1200, 850))

# Name of the game
# pygame.display.set_caption("Write here whatever you want and remove the comment above...")

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

#game loop
while run:
    clock.tick(FPS)

    backgroundImage = pygame.image.load("./images/Table.png")
    window.blit(backgroundImage, (0,0))

    window.blit(pygame.image.load("./images/Joker.png"), (10, 10))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
