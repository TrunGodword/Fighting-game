import sys, pygame, menu, player, collision, settings


def run_game():
    pygame.init()

    player1 = player.Player(100, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, (255, 0, 0), 100, pygame.K_j)
    player2 = player.Player(500, 100, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, (0, 255, 0), 100, pygame.K_k)

    font = pygame.font.Font(None, 32)
    text1 = font.render(str(player1.jumpcd), True, (255,255,255))
    text1_rect = text1.get_rect(center=(32, 32))
    text2 = font.render(str(player1.jumping), True, (255,255,255))
    text2_rect = text2.get_rect(center=(132, 32))
    
    text3 = font.render(str(player2.jumpcd), True, (255,255,255))
    text3_rect = text3.get_rect(center=(settings.maxWidth-32, 32))
    text4 = font.render(str(player2.jumping), True, (255,255,255))
    text4_rect = text4.get_rect(center=(settings.maxWidth-132, 32))

    all_sprites = pygame.sprite.Group(player1, player2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == player1.attackA:
                    text1 = font.render(str(player1.jumpcd), True, (255,255,255))
                    text2 = font.render(str(player1.jumping), True, (255,255,255))
                elif event.key == player2.attackA:
                    text3 = font.render(str(player2.jumpcd), True, (255,255,255))
                    text4 = font.render(str(player2.jumping), True, (255,255,255))

        for value in range(0, len(collision.arrays)):
            for value2 in range(0, len(collision.arrays)):
                pygame.draw.rect(collision.surface, (0,0,255), collision.surface.get_rect(), 3)
                collision.lines[value].append(collision.surface)
                collision.screen.blit(collision.lines[value][value2], (collision.arrays[value][value2][0], collision.arrays[value][value2][1]))

        settings.clock.tick(60)
        all_sprites.update()
        settings.screen.blit(text1, text1_rect)
        settings.screen.blit(text2, text2_rect)
        settings.screen.blit(text3, text3_rect)
        settings.screen.blit(text4, text4_rect)
        all_sprites.draw(settings.screen)
        pygame.display.flip()

run_game()