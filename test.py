import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Gauge Test")

black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pygame.draw.circle(screen, white, (400, 300), 200, 3)
    pygame.display.flip()

pygame.quit()