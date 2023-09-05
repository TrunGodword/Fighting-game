import sys, pygame

screen = pygame.display.set_mode((1024, 768))

def attackArea():
    print("Much to be done here")

class Idle(pygame.sprite.Sprite):
    def __init__(self, speed):
        self.image1 = pygame.image.load("./assets/Samurai/idle1.png")
        self.image2 = pygame.image.load("./assets/Samurai/idle2.png")
        self.image3 = pygame.image.load("./assets/Samurai/idle3.png")
        self.image4 = pygame.image.load("./assets/Samurai/idle4.png")
        self.image5 = pygame.image.load("./assets/Samurai/idle5.png")
        self.image6 = pygame.image.load("./assets/Samurai/idle6.png")
        self.frames = [0, 1, 2, 3, 4, 5, 6]

    def play(self):
        self.rect = self.image1
        self.rect.topleft = [200,300]
        # for frame in self.frames:
        #     match frame:
        #         case 1:
        #             print("Huh?")

moving_sprites = pygame.sprite.Group()
animate = Idle(100,100)
moving_sprites.add(animate)



def animationHandler():
    pygame.init()
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    animate.play()
        

        clock.tick(60)	
        screen.fill((122,122,122))
        screen.fill((122,122,122))
        moving_sprites.draw(screen)
        moving_sprites.update(0.1)
            
animationHandler()