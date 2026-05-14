import pygame
from mouseTracker import *
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main Page")

clock = pygame.time.Clock()

#font
font = pygame.font.Font("fonts/arcadeclassic.regular.ttf", 24)

#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 200, 100)

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

    for i in range(0, MAX_SPEED + 1, 20):
        angle = speedToAngle(i)
        label_radius = radius - 35
        lx = center[0] + label_radius * math.cos(angle)
        ly = center[1] - label_radius * math.sin(angle)

        label = font.render(str(i), True, white)
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


#tachometer
MIN_RPM = 0
MAX_RPM = 8000
REDLINE_RPM = 7000
BAR_WIDTH = 20
BAR_HEIGHT = 400
BAR_X = 100
BAR_Y = 100
TICK_WIDTH = 10

def drawTachometer(surface, rpm):
    pygame.draw.rect(surface, white, (BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT))

    #drawing redline area
    redline_fill = int(BAR_HEIGHT * (1300 / 8000))
    pygame.draw.rect(surface, red, (BAR_X, BAR_Y, BAR_WIDTH, redline_fill))

    ratio = rpm / MAX_RPM
    fill_height = int(BAR_HEIGHT * ratio)
    fill_y = BAR_Y + BAR_HEIGHT - fill_height

    if rpm >= REDLINE_RPM:
        color = red
    else:
        color = green
    
    pygame.draw.rect(surface, color, (BAR_X, fill_y, BAR_WIDTH, fill_height))

    #drawing tick marks
    for i in range(0, MAX_RPM, 1000):
        ratio = i / MAX_RPM
        tick_height = int(BAR_HEIGHT * ratio)
        tick_y = BAR_Y + BAR_HEIGHT - tick_height

        pygame.draw.line(surface, black, (BAR_X, tick_y), (BAR_X + TICK_WIDTH, tick_y))
        
        tick_label = font.render(f"{(i // 1000)}", True, white)
        tick_rect = tick_label.get_rect(center=((BAR_X - 15), tick_y))
        surface.blit(tick_label, tick_rect)

    title = font.render("RPM", True, white)
    title_rect = title.get_rect(center=((BAR_X + BAR_WIDTH // 2), (BAR_Y - 20)))
    surface.blit(title, title_rect)

    rpm_label = font.render(f"{rpm}", True, white)
    rpm_rect = rpm_label.get_rect(center=((BAR_X + BAR_WIDTH //2), (BAR_Y + BAR_HEIGHT + 20)))
    surface.blit(rpm_label, rpm_rect)




#defaults / debug
rpm = 0
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
    drawTachometer(screen, rpm)
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
    rpm += flip * 60

pygame.quit()