import pygame

black = (0, 0, 0)
white = (255, 255, 255)
gray = (150, 150, 150)

def drawGrid(surface):
    for x in range(0, surface.get_width(), 50):
        pygame.draw.line(surface, gray, (x, 0), (x, surface.get_height()), 1)
    for y in range(0, surface.get_height(), 50):
        pygame.draw.line(surface, gray, (0, y), (surface.get_width(), y), 1)

def trackMouse(surface):
    font = pygame.font.Font(None, 24)
    mouse_pos = pygame.mouse.get_pos()
    text = font.render(f"{mouse_pos}", True, white)
    coords = (mouse_pos[0], mouse_pos[1] - 10)
    text_rect = text.get_rect(topleft=coords)
    padded_rect = text_rect.inflate(10, 6)
    pygame.draw.rect(surface, black, padded_rect)
    pygame.draw.rect(surface, white, padded_rect, width=2)
    surface.blit(text, coords)