import pygame
from .constants import RED, BLUE
from checkers.board import Board

class Game:
    def __init__(self, draughts,DIFFICULTY):
        self.draughts =draughts
        self.selected = None
        self.board = Board(DIFFICULTY)
        self.turn = RED
        self.available_moves = {}
        self.DIFFICULTY=DIFFICULTY
        self.Regicide=0
        #print("game start with DIFFICULTY",DIFFICULTY)


    def update(self):
        self.board.draw(self.draughts)
        self.board.draw_available_moves(self.draughts,self.available_moves)

        pygame.display.update()

    #get winner
    def get_winner(self):
        return self.board.get_winner()

    # set the first turn to be red piece
    def reset(self):
        self.selected = None

        self.board = Board()
        self.turn = RED
        self.available_moves = {}

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)

            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        #print(piece)

        if piece != 0 and piece.color == self.turn:

            self.selected = piece
            self.available_moves = self.board.get_available_moves(piece)
            return True

        if self.Regicide==1:
                self.board.be_crowned(piece)
                self.Regicide=0

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.available_moves:
            self.board.move(self.selected, row, col)
            captured = self.available_moves[(row, col)]

            if captured:
                regicide = self.board.capturing(captured)
                if regicide == 1:
                    self.Regicide=1

            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        self.available_moves = {}
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED



    def get_board(self):
        return self.board


    def get_level(self,DIFFICULTY):
        Board.evaluate()
        print(self.DIFFICULTY)
        return DIFFICULTY

    def ai_move(self,board):
        self.board = board
        self.change_turn()
