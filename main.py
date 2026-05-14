import pygame
import math

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main Page")

clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
red = (255, 0, 0)

#speedometer
center = (400, 400)
radius = 200
MIN_SPEED = 0
MAX_SPEED = 120
MIN_ANGLE = 225
MAX_ANGLE = 45

def speedToAngle(speed):
    ratio = speed/MAX_SPEED
    angle = MIN_ANGLE - ratio * (MIN_ANGLE - MAX_ANGLE) - 360 * (ratio > (MIN_ANGLE / 360)) #45
    return math.radians(angle)

def drawGauge(surface, speed):
    pygame.draw.circle(surface, white, center, radius, 3)

    for i in range(0, MAX_SPEED + 1, 10):
        angle = speedToAngle(i) #5pi/4
        inner = radius - 20 # 180
        outer = radius - 5 # 205

        x1 = center[0] + inner * math.cos(angle)
        y1 = center[1] - inner * math.sin(angle) 
        x2 = center[0] + outer * math.cos(angle)
        y2 = center[1] - outer * math.sin(angle)

        pygame.draw.line(surface, gray, (x1, y1), (x2, y2))

    needle_angle = speedToAngle(speed) # 0.7854
    needle_length = radius - 30 # 170
    nx = center[0] + needle_length * math.cos(needle_angle) # 570
    ny = center[1] + needle_length * math.sin(needle_angle) # 402
    pygame.draw.line(surface, red, center, (nx, ny), 3)

    pygame.draw.circle(surface, red, center, 8)

speed = 80


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    drawGauge(screen, speed)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()