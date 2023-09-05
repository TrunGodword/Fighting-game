import sys, pygame, settings, screen1, screen3


def run_game():
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        match settings.screenNum:
            case 1:
                screen1.screen1()
            case 2:
                print("Much to be done here")
            case 3:
                screen3.menu()

run_game()