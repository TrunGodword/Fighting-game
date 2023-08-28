import sys, pygame, menu, player, collision, settings


def run_game():
#~~~Хэсэг 1: Анх програм нээхэд уншигдах value ба variables:
    # Pygame ба тухайн программийн өөрийн цаг буюу уншигдах хурд. Жишээ нь: 1 секүнд бүрт 1000 frame
    pygame.init()
    
    

    player1 = player.Player(100, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, (255, 0, 0), 100, pygame.K_j)
    player2 = player.Player(500, 100, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, (0, 255, 0), 100, pygame.K_k)
    # Дэлгэцний тохиргоо. Өргөн нь 640, урт нь 480

    
    # Цонхны дээр гарж ирэх Application-ий нэрийг солих. Жишээ нь: "Fighting Game"

    font = pygame.font.Font(None, 32)
    text1 = font.render(str(player1.jumpcd), True, (0, 0, 0))
    text1_rect = text1.get_rect(center=(32, 32))
    text2 = font.render(str(player1.jumping), True, (0, 0, 0))
    text2_rect = text2.get_rect(center=(132, 32))

    # text1 = menu.Text("Play", screen_width/2, screen_height/2 - 100, (0, 0, 0))
    # text2 = menu.Text("Settings", screen_width/2, screen_height/2, (0, 0, 0))
    # text3 = menu.Text("Quit", screen_width/2, screen_height/2 + 100, (0, 0, 0))

    # Player 1 ба 2-т Player гэдэг Class-ийг хуваарьлан, тус тусд нь өөрийн гэсэн тохиргоог нь хаалтан дотор бичих.
    # Бүх player-уудыг нэг групп дотор оруулах. Ингэж байгаа нь дараа нь player хоорондын харьцааг илүү амархан тохируулах боломжтой болгож байгаа вм.
    all_sprites = pygame.sprite.Group(player1, player2)

    # Text үүсгээд, утганд нь тухайн player-үүдийн амийг шилжүүлж өгж байгаа нь.
    
    # text_sprites = (pygame.sprite.Group(text1, text2, text3))
    
#~~~Хэсэг 2: Update хийгдэх хэсэн буюу тоглоомны гол EVENT LOOP:
    while True:
        for event in pygame.event.get():
            # Тоглоомыг хаагдаж болгодог өгөгдөл.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == player1.attackA:
                    text1 = font.render(str(player1.jumpcd), True, (0, 0, 0))
                    text2 = font.render(str(player1.jumping), True, (0, 0, 0))

            # Хэрвээ Player1 эсвэл Player2 тус тусын дайралт хийдэг товч буюу J/K-г дарвал өрсөлдөгчийн амь нь буурах.
            # Бас дээрээс нь өрсөлдөгчийн амийг хадгалсан text-ийг update хийж өгөх


        
#~~~Хэсэг 3: Draw буюу бүх өгөгдлүүдийг дэлгэцэн дээр зурах:
        # АНХААРАХ ЗҮЙЛ: Яг ямар дараагаар бичнэ, яг тэр дарааллаар зурж эхэлнэ. Жишээ нь: Дэлгэцний өнгийг хамгийн сүүлд нь зурвал 
        # дэлгэцийг тэр өнгө нь бүрэн бүрхэх ба өмнө нь зурагдсан өгөгдлүүд харагдахгүй.
        
        # Дэлгэцний ард талд өнгө оруулж өгөх.
        settings.screen.fill((255, 255, 255))
        # Text болгонд өндөр ба уртыг хуваарьлан зурах.

        # screen.blit(text1.text, text1.position)
        # screen.blit(text2.text, text2.position)
        # screen.blit(text3.text, text3.position)

        # Секүнд бүрт уншигдах frame-ийг 60 буюу хамгийн их хэрэглэгддэг тогтмол frame-ээр хязгаарлаж өгөх.
        settings.clock.tick(60)
        all_sprites.update()
        settings.screen.blit(text1, text1_rect)
        settings.screen.blit(text2, text2_rect)
        # Эцэст нь screen буюу дэлгэцийг зурна.
        all_sprites.draw(settings.screen)
        # text_sprites.draw(screen)
        pygame.display.flip()



run_game()