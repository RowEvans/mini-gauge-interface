import pygame
from mouseTracker import *
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main Page")

clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
red = (255, 0, 0)

#speedometer
center = (400, 300)
radius = 200
MIN_SPEED = 0
MAX_SPEED = 120
MIN_ANGLE = 225
MAX_ANGLE = 0

#returns the angle (radians) of a certain speed
def speedToAngle(speed):
    ratio = speed/MAX_SPEED
    angle = MIN_ANGLE - ratio * (MIN_ANGLE - MAX_ANGLE)
    return math.radians(angle)

#main drawing function of the speedometer
def drawSpeedometer(surface, speed):
    pygame.draw.circle(surface, white, center, radius, 3)

    for i in range(0, MAX_SPEED + 1, 10):
        angle = speedToAngle(i)
        inner = radius - 20
        outer = radius - 5 

        x1 = center[0] + inner * math.cos(angle)
        y1 = center[1] - inner * math.sin(angle) 
        x2 = center[0] + outer * math.cos(angle)
        y2 = center[1] - outer * math.sin(angle)

        pygame.draw.line(surface, gray, (x1, y1), (x2, y2))

    label_font = pygame.font.Font("fonts/arcadeclassic.regular.ttf", 24)
    for i in range(0, MAX_SPEED + 1, 20):
        angle = speedToAngle(i)
        label_radius = radius - 35
        lx = center[0] + label_radius * math.cos(angle)
        ly = center[1] - label_radius * math.sin(angle)

        label = label_font.render(str(i), True, white)
        label_rect = label.get_rect(center=(lx, ly))
        surface.blit(label, label_rect)
    
    needle_angle = speedToAngle(speed)
    needle_length = radius - 30
    nx = center[0] + needle_length * math.cos(needle_angle)
    ny = center[1] - needle_length * math.sin(needle_angle)
    pygame.draw.line(surface, red, center, (nx, ny), 5)

    speed_font = pygame.font.Font("fonts/arcadeclassic.regular.ttf", 36)
    speed_label = speed_font.render(f"{speed}", True, white)
    speed_rect = speed_label.get_rect(center=center)
    speed_rect_padded = speed_rect.inflate(10, 10)
    pygame.draw.rect(surface, black, speed_rect_padded)
    surface.blit(speed_label, speed_rect)


speed = 0
flip = 1
debug_mode = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                debug_mode = not debug_mode

    screen.fill(black)
    drawSpeedometer(screen, speed)
    if debug_mode:
        drawGrid(screen)
        trackMouse(screen)
    pygame.display.flip()
    clock.tick(60)

    if speed > MAX_SPEED:
        flip = -1
    if speed < MIN_SPEED:
        flip = 1
    
    speed += flip

pygame.quit()