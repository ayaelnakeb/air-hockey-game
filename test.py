import pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pygame Test')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
