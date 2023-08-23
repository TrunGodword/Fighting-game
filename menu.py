import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, input, x, y, color):
        super().__init__()
        self.image = pygame.Surface((100, 100))

        font = pygame.font.Font(None, 32)
        self.text = font.render(str(input), True, color)
        self.position = self.text.get_rect(center=(x, y))
