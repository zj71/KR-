import pygame
from tkinter import *
from tkinter import messagebox

from checkers.constants import WIDTH, HEIGHT, CHECKER_BOARD,BLUE
from checkers.game import Game
from AI.algorithm import alpha_beta

import victory


draughts = pygame.display.set_mode((WIDTH+50, HEIGHT))
pygame.display.set_caption('Checker game by Agnesia')

rules="Checkers game board has eight columns and eight rows."\
      "\nIn this game, human is Red piece(down side of board) and AI is BLUE piece(up side of board)." \
      "\n1. Click on a piece to move it around the board." \
      "\n2. Black moves first, and play proceeds alternately." \
      "\n *checkers may only move forward." \
      "\n *There are two types of moves that can be made: capturing and non-capturing ." \
      "\n *Non-capturing moves are simply a diagonal move forward from one square to an adjacent square." \
      "\n *Capturing moves occur when a player “jumps” an opposing piece. "\
      "\n3. Multi-leg capturing is available which means a piece may make multiple jumps."\
      "\n4. This game FORCE CAPTURE and reject the INVAILD MOVES."\
      "\n5. When a piece achieves the opponent’s edge of the board ,it will become a KING."\
      "\n6. The object is to eliminate all opposing checkers or capture a king(REGICIDE)."





def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // CHECKER_BOARD
    col = x // CHECKER_BOARD
    return row, col

def main(DIFFICULTY):
    run = True
    clock = pygame.time.Clock()
    game = Game(draughts,DIFFICULTY)


    while run:
        clock.tick(0)
        alpha = -float('inf')
        beta= float('inf')
        mouse = pygame.mouse.get_pos()



        if game.turn == BLUE:
            #use algorthim
            value, new_board ,alpha,beta= alpha_beta(game.get_board(),4,BLUE,game,alpha,beta)

            #update board
            #print("alpha",alpha)
            #print("bate",beta)
            game.ai_move(new_board)

        if game.get_winner() != None:
           #print(game.winner())
           victory.winner_page(game.get_winner())
           run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if mouse[0] < 600  and event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_row_col_from_mouse(mouse)
                game.select(row, col)
                #app.event(event)

            if mouse[0] >= 600 and mouse[1] <= 200 and event.type == pygame.MOUSEBUTTONDOWN:
                    Tk().wm_withdraw() #to hide the main window
                    messagebox.showinfo('Rules',rules)

            if mouse[0] >= 600 and mouse[1] >= 400 and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()


        game.update()


    #pygame.quit()


#main(2)

