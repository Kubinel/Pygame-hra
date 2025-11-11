import pygame

pygame.init()
pygame.display.set_caption("My Pygame Window")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
