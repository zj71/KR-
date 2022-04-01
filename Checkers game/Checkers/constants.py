import pygame
pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
CHECKER_BOARD = WIDTH//COLS#100
RADIUS_PIECE =30
DIFFICULTY = 1

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (233, 212, 96)
SILVER = (192,192,192)

#font
FONT_WIN= pygame.font.Font('./Font/JOKERMAN.TTF', 60)
FONT= pygame.font.Font('./Font/RAVIE.TTF', 20)

#image
IM_START = pygame.transform.scale(pygame.image.load("./images/s1.jpg"),
                                  (650,100))
IM_TITLE = pygame.transform.scale(pygame.image.load("./images/title.jpg"),
                                  (650,300))
KING =pygame.transform.scale(pygame.image.load("./images/kings.png"),
                                  (100,100))
VICTORY = pygame.transform.scale(pygame.image.load("./images/victory.png"),
                                  (650,300))
RULE = pygame.transform.scale(pygame.image.load("./images/rule.png"),
                                  (50,200))
QUIT = pygame.transform.scale(pygame.image.load("./images/quit.png"),
                                  (50,200))




