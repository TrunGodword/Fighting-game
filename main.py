import sys, pygame, menu, player, collision, settings


def run_game():
    pygame.init()

    player1 = player.Player(100, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, (255, 0, 0), 100, pygame.K_j, 50, 70)
    player2 = player.Player(500, 100, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, (0, 255, 0), 100, pygame.K_k, 50, 70)


    font = pygame.font.Font(None, 32)
    text1 = font.render(str(player1.jumpcd), True, (255,255,255))
    text1_rect = text1.get_rect(center=(32, 32))
    text2 = font.render(str(player1.jumping), True, (255,255,255))
    text2_rect = text2.get_rect(center=(150, 32))
    text3 = font.render(str(player2.jumpcd), True, (255,255,255))
    text3_rect = text3.get_rect(center=(settings.maxWidth/2 -180, 132))
    text4 = font.render(str(player2.jumping), True, (255,255,255))
    text4_rect = text4.get_rect(center=(232, 32))
    text5 = font.render(str(player1.jumpcd), True, (255,255,255))
    text5_rect = text5.get_rect(center=(settings.maxWidth - 32, 32))
    text6 = font.render(str(player1.jumping), True, (255,255,255))
    text6_rect = text6.get_rect(center=(settings.maxWidth - 132, 32))
    text7 = font.render(str(player2.jumpcd), True, (255,255,255))
    text7_rect = text7.get_rect(center=(settings.maxWidth - 232, 32))

    text8 = font.render(str(player1.jumpcd), True, (255,255,255))
    text8_rect = text8.get_rect(center=(32, 82))
    text9 = font.render(str(player1.jumping), True, (255,255,255))
    text9_rect = text9.get_rect(center=(150, 82))
    text10 = font.render(str(player2.jumpcd), True, (255,255,255))
    text10_rect = text10.get_rect(center=(232, 82))
    text11 = font.render(str(player2.jumping), True, (255,255,255))
    text11_rect = text11.get_rect(center=(settings.maxWidth - 32, 82))
    text12 = font.render(str(player1.jumpcd), True, (255,255,255))
    text12_rect = text12.get_rect(center=(settings.maxWidth - 132, 82))
    text13 = font.render(str(player1.jumping), True, (255,255,255))
    text13_rect = text13.get_rect(center=(settings.maxWidth - 232, 82))

    playerObjects = [player1, player2]
    playerGroup = pygame.sprite.Group(playerObjects)
    
    pygame.draw.rect(collision.surface, (0,0,255), collision.surface.get_rect(), 3)
   

    while True:
        text1 = font.render(str(player1.rect.x), True, (255,255,255))
        text2 = font.render(str(collision.checkCollision(playerObjects)[0]), True, (255,255,255))
        text3 = font.render(str(collision.xlines), True, (255,255,255))
        text4 = font.render(str(collision.checkCollision(playerObjects)[1]), True, (255,255,255))
        text5 = font.render(str(player2.rect.x), True, (255,255,255))
        text6 = font.render(str(collision.checkCollision(playerObjects)[4]), True, (255,255,255))
        text7 = font.render(str(collision.checkCollision(playerObjects)[5]), True, (255,255,255))

        text8 = font.render(str(player1.rect.y), True, (255,255,255))
        text9 = font.render(str(collision.checkCollision(playerObjects)[2]), True, (255,255,255))
        text10 = font.render(str(collision.checkCollision(playerObjects)[3]), True, (255,255,255))
        text11 = font.render(str(player2.rect.y), True, (255,255,255))
        text12 = font.render(str(collision.checkCollision(playerObjects)[6]), True, (255,255,255))
        text13 = font.render(str(collision.checkCollision(playerObjects)[7]), True, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        for value in range(0, len(collision.arrays)):
            for value2 in range(0, len(collision.arrays)):
                collision.lines[value].append(collision.surface)
                collision.screen.blit(collision.lines[value][value2], (collision.arrays[value][value2][0], collision.arrays[value][value2][1]))

        settings.clock.tick(60)
        playerGroup.update()
        settings.screen.blit(text1, text1_rect)
        settings.screen.blit(text2, text2_rect)
        settings.screen.blit(text3, text3_rect)
        settings.screen.blit(text4, text4_rect)
        settings.screen.blit(text5, text5_rect)
        settings.screen.blit(text6, text6_rect)
        settings.screen.blit(text7, text7_rect)
        settings.screen.blit(text8, text8_rect)
        settings.screen.blit(text9, text9_rect)
        settings.screen.blit(text10, text10_rect)
        settings.screen.blit(text11, text11_rect)
        settings.screen.blit(text12, text12_rect)
        settings.screen.blit(text13, text13_rect)
        playerGroup.draw(settings.screen)
        pygame.display.flip()

run_game()