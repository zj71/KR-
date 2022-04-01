import pygame
from checkers.constants import WIDTH, HEIGHT,BLACK ,RED,VICTORY,BLUE,WHITE,FONT_WIN


def winner_page(winner):


    text_Win_R = FONT_WIN.render("winner is HUMAN !", False, WHITE)
    text_Win_B = FONT_WIN.render("winner is AI !", False, WHITE)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
    #  create victiry window

        wp = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('victory Page')


        wp.fill(BLACK)
        wp.blit(VICTORY, (0,0))
        if winner ==RED:
            wp.blit(text_Win_R, (20,350))
        if winner ==BLUE:
            wp.blit(text_Win_B, (120,350))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pygame.display.update()

    pygame.mouse.get_pos()




#winner_page(BLUE)
