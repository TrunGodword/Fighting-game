import pygame
import settings

screen = settings.pygame.display.get_surface()

width, height = screen.get_width(), screen.get_height()

width /= 8
height /= 8
for value in range(1, 9):
    print(value)