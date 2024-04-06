import pygame
import win32api
import math
from transparent import go_transparent
from calc import left_svt_flash_points, right_svt_flash_points
from time import perf_counter


width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
done = False
colorkey = (69, 42, 0)
start = perf_counter()

go_transparent(colorkey)
#           Rea-  (stop)dy- (stop)  Get  Set  Go!
intervals = [0.6, 0.7, 1.2, 1.3, 1.8, 2.4, 3.0, 10]
ev = 0
while not done:
    now = perf_counter()
    elasped = now - start
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(colorkey)

    if intervals and elasped - 2 >= intervals[0]:
        ev += 1
        intervals.pop(0)
    match ev:
        case 1 | 3:
            pygame.draw.polygon(
                screen,
                (255, 255, 255),
                left_svt_flash_points(width, height, 20, -math.sin(elasped * 2) * 15 + 30, 30)
            )
            pygame.draw.polygon(
                screen,
                (255, 255, 255),
                right_svt_flash_points(width, height, 20, math.sin(elasped * 2) * 15 - 30, 30)
            )
        case 2 | 4:
            ...
        case 5:
            pygame.draw.polygon(
                screen,
                (255, 255, 255),
                left_svt_flash_points(width, height, 20, -math.sin(elasped * 2) * 15 + 30, 30)
            )
        case 6:
            pygame.draw.polygon(
                screen,
                (255, 255, 255),
                left_svt_flash_points(width, height, 20, -math.sin(elasped * 2) * 15 + 30, 30)
            )
            pygame.draw.polygon(
                screen,
                (255, 255, 255),
                right_svt_flash_points(width, height, 20, math.sin(elasped * 2) * 15 - 30, 30)
            )
        case 7:
            intervals = [0.6, 0.7, 1.2, 1.3, 1.8, 2.4, 3.0, 10]
            start = perf_counter()
    
    if win32api.GetAsyncKeyState(ord('R')):
        intervals = [0.6, 0.7, 1.2, 1.3, 1.8, 2.4, 3.0, 10]
        ev = 0
        start = perf_counter()
    pygame.display.update()