import sys, pygame, settings

screen = pygame.display.set_mode((1024, 768))

def attack2():
    images = [pygame.image.load(f"./assets/Samurai/death{i}.png") for i in range(1, 7)]
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for frame in frames:
        match frame:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                screen.blit(images[0], (512, 384))
            case 1:
                screen.blit(images[0], (512, 384))
            case 2:
                screen.blit(images[0], (512, 384))
            case 3:
                screen.blit(images[1], (512, 384))
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                screen.blit(images[1], (512, 384))
            case 5:
                screen.blit(images[1], (512, 384))
            case 6:
                screen.blit(images[2], (512, 384))
            case 7:
                screen.blit(images[2], (512, 384))
            case 8:
                screen.blit(images[2], (512, 384))
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                screen.blit(images[3], (512, 384))
            case 10:
                screen.blit(images[3], (512, 384))
            case 11:
                screen.blit(images[3], (512, 384))
            case 12:
                screen.blit(images[4], (512, 384))
            case 13:
                screen.blit(images[4], (512, 384))
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                screen.blit(images[4], (512, 384))
            case 15:
                screen.blit(images[5], (512, 384))
            case 16:
                screen.blit(images[5], (512, 384))
        yield

def attack1(posx, posy):
    images = [pygame.image.load(f"./assets/Samurai/idle{i}.png") for i in range(1, 7)]
    frames = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for value in range(0, len(frames)):
        match value:
            case 0:
                # hitbox info here, for example, (220,200)
                jumpable = False # So that the player can jump cancel the animation at a certain point
                screen.blit(images[0], (posx, posy))
            case 1:
                screen.blit(images[0], (posx, posy))
            case 2:
                screen.blit(images[0], (posx, posy))
            case 3:
                screen.blit(images[1], (posx, posy))
            case 4:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                screen.blit(images[1], (posx, posy))
            case 5:
                screen.blit(images[1], (posx, posy))
            case 6:
                screen.blit(images[2], (posx, posy))
            case 7:
                screen.blit(images[2], (posx, posy))
            case 8:
                screen.blit(images[2], (posx, posy))
            case 9:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                screen.blit(images[3], (posx, posy))
            case 10:
                screen.blit(images[3], (posx, posy))
            case 11:
                screen.blit(images[3], (posx, posy))
            case 12:
                screen.blit(images[4], (posx, posy))
            case 13:
                screen.blit(images[4], (posx, posy))
            case 14:
                # Then, attacking area, for example, attackArea(playerx + 200, player.y + 60, 200, 400) etc.
                screen.blit(images[4], (posx, posy))
            case 15:
                screen.blit(images[5], (posx, posy))
            case 16:
                screen.blit(images[5], (posx, posy))
        yield

def animationHandler():
    pygame.init()
    clock = pygame.time.Clock()
    attack = None
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    attack = attack1(settings.maxWidth/2, settings.maxHeight/2)
                elif event.key == pygame.K_k:
                    attack = attack2()
        if attack:
            try:
                next(attack)
            except StopIteration:
                attack = None

        clock.tick(60)
        pygame.display.update()
        pygame.display.flip()

animationHandler()
