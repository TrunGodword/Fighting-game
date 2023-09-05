import pygame, settings, sys
from util import load_save, reset_keys
from controls import Controls_Handler

def run():
################################# LOAD UP A BASIC WINDOW #################################
    pygame.init()
    screen = pygame.display.set_mode(((1024,768)))
    maxWidth, maxHeight = screen.get_width(), screen.get_height()
    canvas = pygame.Surface((maxWidth/2,maxHeight/2))
    running = True
    actions = {"Left": False, "Right": False, "Up": False, "Down": False, "Start": False, "Action1": False}
################################ LOAD THE CURRENT SAVE FILE #################################
    save = load_save()
    control_handler = Controls_Handler(save)
    ################################# GAME LOOP ##########################
    while running:
        ################################# CHECK PLAYER INPUT #################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings.screenNum = 3
                    running = False
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = True
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = True
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = True
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = True
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = True
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = True
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = True


            if event.type == pygame.KEYUP:
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = False
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = False
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = False
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = False
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = False
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = False

    ################################# UPDATE THE GAME #################################
        control_handler.update(actions)
        ################################# RENDER WINDOW AND DISPLAY #################################
        canvas.fill((135, 206, 235))
        control_handler.render(canvas)
        screen.blit(pygame.transform.scale(canvas, (maxWidth,maxHeight) ), (0,0))
        pygame.display.update()
        reset_keys(actions)