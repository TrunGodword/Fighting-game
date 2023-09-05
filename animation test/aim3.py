import pygame, sys, frames3

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		
		self.image = frames3.sprites[frames3.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			frames3.current_sprite += speed
			if int(frames3.current_sprite) >= len(frames3.sprites):
				frames3.current_sprite = 4
				self.attack_animation = False

		self.image = frames3.sprites[int(frames3.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			player.current_sprite = 0
			player.attack()
			

	# Drawing
	screen.fill((122,122,122))
	moving_sprites.draw(screen)
	moving_sprites.update(0.1)
	pygame.display.flip()
	clock.tick(60)