from .constants import CHECKER_BOARD, KING,RADIUS_PIECE, RED, BLUE
import pygame

class Piece:

    def __init__(self, row, col, color):
        #y = row
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.Regicide=False
        #[downside_red,downside_blue,upside_red,upside_blue/not king ] 0 is false
        self.current_state=[0,0,0,0]
        self.position()

    #calculate the position
    def position(self):

        self.x = CHECKER_BOARD * self.col + CHECKER_BOARD // 2
        self.y = CHECKER_BOARD * self.row + CHECKER_BOARD // 2
        if self.color==RED:
            if self.y >= 300:
                self.current_state[0] = 1
                self.current_state[2] = 0
            else:
                self.current_state[2] = 1
                self.current_state[0] = 0

        if self.color==BLUE:
            if self.y >= 300:
                self.current_state[1] = 1
                self.current_state[3] = 0
            else:
                self.current_state[3] = 1
                self.current_state[1] = 0

    def make_king(self):
        self.king = True

    #draw the piece and add the possible king
    def draw(self,draughts):
        pygame.draw.circle(draughts, self.color, (self.x, self.y), RADIUS_PIECE)
        if self.king:
            draughts.blit(KING, (self.x - KING.get_width()//2, self.y - KING.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.position()


