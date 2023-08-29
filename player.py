import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, up, down, left, right, color, health, attackA, sizex, sizey):
        super().__init__()
        self.image = pygame.Surface((sizex, sizey))
        self.color = (color)
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.speed = 10
        self.health = health
        self.mass = 20
        self.gravity = 10
        self.jumping = False
        self.jumpcd = 40
        self.initialmass = self.mass
        self.dt = round(1/60, 4)
        
        self.up =  up
        self.down = down
        self.left = left
        self.right = right
        self.attackA = attackA
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if self.mass < self.initialmass:
            self.mass += 1
            
        if self.jumping == True and self.jumpcd >= 1:
            self.jumpcd -= 1
        else:
            self.jumping = False
            self.jumpcd = 40
        
        self.rect.y += self.mass + (self.gravity * self.dt)

        if keys[self.left]:
            self.rect.x -= self.speed
        if keys[self.right]:
            self.rect.x += self.speed
        if keys[self.up] and self.jumping == False:
            self.mass = -(self.mass)
            self.jumping = True

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > settings.maxWidth:
            self.rect.right = settings.maxWidth
    
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > settings.maxHeight:
            self.rect.bottom = settings.maxHeight