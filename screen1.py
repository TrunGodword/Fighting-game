import sys, pygame, settings, player, collision


def createText(input, color, size):
    font = pygame.font.Font(None, size)
    text = font.render(str(input), True, (color))
    return text

def play():
    pygame.init()
    player1 = player.Player(100, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, (255, 0, 0), 100, pygame.K_j, 50, 70)
    player2 = player.Player(500, 100, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, (0, 255, 0), 100, pygame.K_k, 50, 70)

    playerObjects = [player1, player2]
    playerGroup = pygame.sprite.Group(playerObjects)
    
    pygame.draw.rect(collision.surface, (0,0,255), collision.surface.get_rect(), 3)
   
    collision.lines[0].append(collision.surface)

    while True:
        objectCollide = collision.checkCollision(playerObjects)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                settings.screenNum = 3
                return
        
        settings.screen.fill((0,0,0))
        # print(objectCollide)
        for value in range(0, 8, 4):
            collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value]][objectCollide[value+1]][0], collision.arrays[objectCollide[value]][objectCollide[value+1]][1]))
            collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value]][objectCollide[value+3]][0], collision.arrays[objectCollide[value]][objectCollide[value+3]][1]))
            collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value+2]][objectCollide[value+1]][0], collision.arrays[objectCollide[value+2]][objectCollide[value+1]][1]))
            collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value+2]][objectCollide[value+3]][0], collision.arrays[objectCollide[value+2]][objectCollide[value+3]][1]))


        settings.clock.tick(60)
        playerGroup.update()
        settings.screen.blit(createText(player1.rect.x, (255,255,255), 36), (32, 32))
        settings.screen.blit(createText(objectCollide[0], (255,255,255), 36), (150, 32))
        settings.screen.blit(createText(collision.xlines, (255,255,255), 36), (settings.maxWidth/2 -180, 132))
        settings.screen.blit(createText(objectCollide[1], (255,255,255), 36), (232, 32))
        settings.screen.blit(createText(player2.rect.x, (255,255,255), 36), (settings.maxWidth - 82, 32))
        settings.screen.blit(createText(objectCollide[4], (255,255,255), 36), (settings.maxWidth - 182, 32))
        settings.screen.blit(createText(objectCollide[5], (255,255,255), 36), (settings.maxWidth - 282, 32))
        settings.screen.blit(createText(player1.rect.y, (255,255,255), 36), (32, 82))
        settings.screen.blit(createText(objectCollide[2], (255,255,255), 36), (150, 82))
        settings.screen.blit(createText(objectCollide[3], (255,255,255), 36), (232, 82))
        settings.screen.blit(createText(player2.rect.y, (255,255,255), 36), (settings.maxWidth - 82, 82))
        settings.screen.blit(createText(objectCollide[6], (255,255,255), 36), (settings.maxWidth - 182, 82))
        settings.screen.blit(createText(objectCollide[7], (255,255,255), 36), (settings.maxWidth - 282, 82))
        playerGroup.draw(settings.screen)
        pygame.display.flip()