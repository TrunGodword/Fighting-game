import sys, pygame, settings, player, collision, animation


def createText(input, color, size):
    font = pygame.font.Font(None, size)
    text = font.render(str(input), True, (color))
    return text

def play():
    pygame.init()
    player1 = player.Player(100, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, (255, 0, 0), 100, pygame.K_l, 80, 130, 45)
    player2 = player.Player(500, 100, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, (0, 255, 0), 100, pygame.K_k, 80, 130, 85)
    
    
    flipped2 = 1
    flipped1 = 0

    playerObjects = [player1, player2]
    playerGroup = pygame.sprite.Group(playerObjects)
    
    pygame.draw.rect(collision.surface, (0,0,255), collision.surface.get_rect(), 3)
   
    collision.lines[0].append(collision.surface)
    animate = None

    while True:
        settings.screen.blit(pygame.transform.scale(pygame.image.load("./assets/background1.gif"), (settings.maxWidth, settings.maxHeight)), (0, 0))
        objectCollide = collision.checkCollision(playerObjects)
        # for value in range(0, 8, 4):
            # collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value]][objectCollide[value+1]][0], collision.arrays[objectCollide[value]][objectCollide[value+1]][1]))
            # collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value]][objectCollide[value+3]][0], collision.arrays[objectCollide[value]][objectCollide[value+3]][1]))
            # collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value+2]][objectCollide[value+1]][0], collision.arrays[objectCollide[value+2]][objectCollide[value+1]][1]))
            # collision.screen.blit(collision.surface, (collision.arrays[objectCollide[value+2]][objectCollide[value+3]][0], collision.arrays[objectCollide[value+2]][objectCollide[value+3]][1]))
        
        if objectCollide[2] > objectCollide[4]:
            flipped1 = 1
            flipped2 = 0
            # player2.rect = player2.image.get_rect(bottomright = (player2.rect.x, settings.maxHeight - player2.sizey + 130))
        else:
            flipped1 = 0
            flipped2 = 1
            # player1.rect = player1.image.get_rect(bottomright = (player1.rect.x, settings.maxHeight - player1.sizey + 130))
            # player2.rect = player2.image.get_rect(bottomleft = (player2.rect.x, settings.maxHeight - player2.sizey + 130))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                settings.screenNum = 3
                return
                
            elif player1.current_health < 0:
                animate = animation.death(player1, flipped1)
            elif player2.current_health < 0:
                animate = animation.death(player2, flipped2)
                
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case player1.up:
                        animate = animation.jump(player1, flipped1)
                    case player1.right:
                        animate = animation.walk(player1, flipped1)
                    case player1.left:
                        animate = animation.walkBack(player1, flipped2)
                    case pygame.K_f:
                        animate = animation.attack1(player1, flipped1)
                        player2.get_damage(20)
                    case pygame.K_g:
                        animate = animation.attack2(player1, flipped1)
                        player2.get_damage(20)
                    case pygame.K_h:
                        animate = animation.attack3(player1, flipped1)
                        player2.get_damage(20)
                    case pygame.K_r:
                        animate = animation.special1(player1, flipped1)
                        player2.get_damage(20)
                    case pygame.K_t:
                        animate = animation.special2(player1, flipped1)
                        player2.get_damage(20)
                    case pygame.K_y:
                        animate = animation.special3(player1, flipped1)
                        player2.get_damage(20)
                    case player2.up:
                        animate = animation.jump(player2, flipped2)
                    case player2.right:
                        animate = animation.walk(player2, flipped1)
                    case player2.left:
                        animate = animation.walkBack(player2, flipped2)
                    case pygame.K_j:
                        animate = animation.attack1(player2, flipped2)
                        player1.get_damage(20)
                    case pygame.K_k:
                        animate = animation.attack2(player2, flipped2)
                        player1.get_damage(20)
                    case pygame.K_l:
                        animate = animation.attack3(player2, flipped2)
                        player1.get_damage(20)
                    case pygame.K_u:
                        animate = animation.special1(player2, flipped2)
                        player1.get_damage(20)
                    case pygame.K_i:
                        animate = animation.special2(player2, flipped2)
                        player1.get_damage(20)
                    case pygame.K_o:
                        animate = animation.special3(player2, flipped2)
                        player1.get_damage(20)
            
            

        if animate:
            try:
                next(animate)
            except StopIteration:
                animate = None
        
        # print(objectCollide)
        

        settings.clock.tick(60)
        playerGroup.update()
        # settings.screen.blit(createText(flipped1, (255,255,255), 36), (32, 32)) ; settings.screen.blit(createText(flipped2, (255,255,255), 36), (150, 32)) ; settings.screen.blit(createText(collision.xlines, (255,255,255), 36), (settings.maxWidth/2 -180, 132)) ; settings.screen.blit(createText(objectCollide[1], (255,255,255), 36), (232, 32)) ; settings.screen.blit(createText(player2.rect.x, (255,255,255), 36), (settings.maxWidth - 82, 32)) ; settings.screen.blit(createText(objectCollide[4], (255,255,255), 36), (settings.maxWidth - 182, 32)) ; settings.screen.blit(createText(objectCollide[5], (255,255,255), 36), (settings.maxWidth - 282, 32)) ; settings.screen.blit(createText(player1.rect.y, (255,255,255), 36), (32, 82)) ; settings.screen.blit(createText(objectCollide[2], (255,255,255), 36), (150, 82)) ; settings.screen.blit(createText(objectCollide[3], (255,255,255), 36), (232, 82)) ; settings.screen.blit(createText(player2.rect.y, (255,255,255), 36), (settings.maxWidth - 82, 82)) ; settings.screen.blit(createText(objectCollide[6], (255,255,255), 36), (settings.maxWidth - 182, 82)) ; settings.screen.blit(createText(objectCollide[7], (255,255,255), 36), (settings.maxWidth - 282, 82))
        playerGroup.draw(settings.screen)
        pygame.display.flip()