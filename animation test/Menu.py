import pygame 
import sys

#Pygame-г эхлүүлэх
pygame.init()

# Set up display
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Menu')

#Colors
Black = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

#Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface, text_rect)

def main_menu():
    while True:
        screen.fill(Black)
        draw_text('Main Menu ', font, WHITE, 400,100)
        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(300, 200, 200, 50)
        button_settings = pygame.Rect(300, 300, 200, 50)
        button_quit = pygame.Rect(300, 400, 200, 50)

        pygame.draw.rect(screen, RED , button_start)
        pygame.draw.rect(screen,RED, button_settings )
        pygame.draw.rect(screen,RED, button_quit )

        draw_text('START ', font , WHITE , 400, 225)
        draw_text('SETTINGS',font, WHITE , 400, 325 )
        draw_text('QUIT',font, WHITE , 400, 425 )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint((mx, my)):
                    print('Start button clicked')
                if button_settings.collidepoint((mx, my)):
                    settings_menu()
                if button_quit.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def settings_menu():
    while True:
        screen.fill(Black)
        draw_text("Settings", font, WHITE, 400, 100)
        
        mx, my = pygame.mouse.get_pos()
        
        button_back = pygame.Rect(300, 500, 200, 50)
        
        pygame.draw.rect(screen, RED, button_back)
        
        draw_text("Back", font, WHITE, 400, 525)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.collidepoint((mx, my)):
                    return  # Return to the main menu
        
        pygame.display.update()

if __name__ == "__main__":
    main_menu()