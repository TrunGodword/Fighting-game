import sys, pygame, player, collision, settings, screen1, screen2, screen3


def run_game():
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if settings.screenNum == 1:
            screen1.screen1()
        elif settings.screenNum == 2:
            screen2
        elif settings.screenNum == 3:
            screen3.menu()

run_game()