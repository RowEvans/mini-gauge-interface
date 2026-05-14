import pygame

screen = pygame.display.set_mode((1080, 800))
pygame.display.set_caption("Main Page")

black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pygame.draw.circle(screen, white, (540, 400), 200, 5)
    pygame.display.flip()

pygame.quit()