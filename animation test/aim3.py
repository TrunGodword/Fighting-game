import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('./frime3/tack1.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack2.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack3.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack4.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack5.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack6.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack7.gif'))
		self.sprites.append(pygame.image.load('./frime3/tack8.gif'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 4
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

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
	moving_sprites.update(0.05)
	pygame.display.flip()
	clock.tick(60)