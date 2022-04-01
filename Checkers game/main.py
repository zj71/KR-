import pygame
import Game
from checkers.constants import WIDTH, HEIGHT,IM_TITLE,BLACK,IM_START,RED,FONT,WHITE,SILVER

#  create game window
sp = pygame.display.set_mode((WIDTH+50, HEIGHT))
pygame.display.set_caption('Start Page')

sp.fill(BLACK)
sp.blit(IM_START, (0,400))
sp.blit(IM_TITLE, (0,0))

text_notice = FONT.render("AI is blue piece and you will start first", True, RED)
text_notice2 = FONT.render("press level first ,change difficulty", True,WHITE)
text_notice3 = FONT.render("Default difficulty is : MEDIUM", True, RED)
text_notice4 = FONT.render("Then press start ,enjoy game", True,WHITE)
sp.blit(text_notice, (50,500))
sp.blit(text_notice2, (70,520))
sp.blit(text_notice3, (100,540))
sp.blit(text_notice4, (110,560))
pygame.display.update()

def draw_choice(mouse,rect,text):

     if rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1]:
        pygame.draw.rect(sp, SILVER,rect)
        level1 = FONT.render(text, True, RED)
     else:
        pygame.draw.rect(sp, BLACK,rect)
        level1 = FONT.render(text, True, WHITE)

     sp.blit(level1, (rect[3]/2 + rect[0],rect[3]/2 + rect[1]))
     pygame.display.update()


def checkers():
    run = True
    clock = pygame.time.Clock()

    #set default difficulty
    DIFFICULTY=2
    while run:
        clock.tick(60)

        mouse = pygame.mouse.get_pos()
        #print(mouse)

        level_E=(0,300,200,90)
        level_M = (650/3,300,200,90)
        level_H = (650/3*2,300,200,90)
        draw_choice(mouse,level_E,"EASY")
        draw_choice(mouse,level_M ,"MEDIUM")
        draw_choice(mouse,level_H ,"HARD")


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if level_E[0]+level_E[2] > mouse[0] >level_E[0] and level_E[1]+level_E[3] > mouse[1] > level_E[1] and event.type == pygame.MOUSEBUTTONDOWN:
                print("Easy", event)
                DIFFICULTY=1

            if level_M[0]+level_M[2] > mouse[0] >level_M[0] and level_M[1]+level_M[3] > mouse[1] > level_M[1] and event.type == pygame.MOUSEBUTTONDOWN:
                print("Medium", event)
                DIFFICULTY=2

            if level_H[0]+level_H[2] > mouse[0] >level_H[0] and level_H[1]+level_H[3] > mouse[1] > level_H[1] and event.type == pygame.MOUSEBUTTONDOWN:
                print("Hard", event)
                DIFFICULTY=3

            # start game
            if DIFFICULTY==1 or 2 or 3:
                if mouse[0] >= 0 and mouse[0] <= 600 and mouse[1] >= 400 and mouse[1] <=500 and event.type == pygame.MOUSEBUTTONDOWN:
                    gameboard = Game.main(DIFFICULTY)


    pygame.mouse.get_pos()



checkers()



