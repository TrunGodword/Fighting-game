import pygame

screenNum = 3
clock = pygame.time.Clock()
screen_width = [640, 1024, 1920]
screen_height = [480, 768, 1080]
screen = pygame.display.set_mode((screen_width[1], screen_height[1]))
pygame.display.set_caption("Fighting game")

maxWidth, maxHeight = screen.get_width(), screen.get_height()

volume = []

#  Player 1 settings

# p1attack1 = pygame.K_J