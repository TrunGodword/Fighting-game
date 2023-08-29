import pygame

clock = pygame.time.Clock()
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fighting game")

maxWidth, maxHeight = screen.get_width(), screen.get_height()