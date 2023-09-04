import pygame, sys, settings
from screen1 import createText

pygame.init()

def menu():
    global screenNum
    while True:
        settings.screen.fill((0,0,0))
        settings.screen.blit(createText("Fighting Game Project", (255,255,255), 84), (settings.maxWidth/2-320, 70))
        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(365, 200, 300, 100)
        button_settings = pygame.Rect(365, 400, 300, 100)
        button_quit = pygame.Rect(365, 600, 300, 100)

        pygame.draw.rect(settings.screen, (255,0,0) , button_start)
        pygame.draw.rect(settings.screen,(255,0,0), button_settings )
        pygame.draw.rect(settings.screen,(255,0,0), button_quit )

        settings.screen.blit(createText("START", (255, 255, 255), 72), (settings.maxWidth/2-70, 225))
        settings.screen.blit(createText("SETTINGS", (255, 255, 255), 72), (settings.maxWidth/2-120, 425))
        settings.screen.blit(createText("QUIT", (255, 255, 255), 72), (settings.maxWidth/2-50, 625))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint((mx, my)):
                    settings.screenNum = 1
                    print(settings.screenNum)
                    return
                if button_settings.collidepoint((mx, my)):
                    print("Much to be done here")
                if button_quit.collidepoint((mx, my)):
                    sys.exit()

        pygame.display.update()