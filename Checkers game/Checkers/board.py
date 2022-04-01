import pygame


from .constants import BLACK, ROWS, RED, CHECKER_BOARD, COLS, WHITE,BLUE,YELLOW,RULE,QUIT
from .piece import Piece

class Board:
    def __init__(self,DIFFICULTY):
        self.board = []
        self.red_number = self.blue_number = 12
        self.red_kings = self.blue_kings = 0
        self.create_board()
        self.DIFFICULTY=DIFFICULTY
        #print("board with DIFFICULTY",DIFFICULTY)


    # draw the game board
    def draw_board(self, draughts):
        draughts.fill(BLACK)
        draughts.blit(RULE, (600,0))
        draughts.blit(QUIT, (600,400))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(draughts, WHITE, (row*CHECKER_BOARD, col *CHECKER_BOARD,CHECKER_BOARD, CHECKER_BOARD))


# draw the basic of board
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLUE))
                        #print(Piece(row, col, BLUE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

        #print(self.board)

    #draw the pieces and board
    def draw(self, draughts):
        self.draw_board(draughts)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(draughts)

    #draw vaild moves
    def draw_available_moves(self, draughts,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(draughts, YELLOW, (col * CHECKER_BOARD + CHECKER_BOARD//2, row * CHECKER_BOARD + CHECKER_BOARD//2), 15)

    # do the move action and check if it's a king
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            self.be_crowned(piece)

    def  be_crowned(self,piece):
        if piece.king == False:
                piece.make_king()
                if piece.color == BLUE:
                    self.blue_kings += 1
                else:
                    self.red_kings += 1


    def ai_skip(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_number -= 1
                else:
                    self.blue_number -= 1

#return like : <checkers.piece.Piece object at 0x0000023268BB45E0>
    def get_piece(self, row, col):
        return self.board[row][col]


    # do capturing
    def capturing(self, pieces):
        rigicide = 0
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_number -= 1
                else:
                    self.blue_number -= 1

                #if king can Regicide
                if piece.king == True:
                    rigicide = 1
                    #print("game over")
        return rigicide




    def get_winner(self):
        if self.red_number <= 0 :
            return BLUE
        elif self.blue_number <= 0 :
            return RED

        return None

    # do valid moves
    def get_available_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self.left_iteration(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self.right_iteration(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == BLUE or piece.king:
            moves.update(self.left_iteration(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self.right_iteration(row +1, min(row+3, ROWS), 1, piece.color, right))
        #print(moves)
        return moves

    def left_iteration(self, start, stop, step, color, left, captured=[]):
        ''' make a left iteration to get

        :param start:current position of piece
        :param stop:how many rows will expand
        :param direction:direction of piece, direction of upper piece is 1 and another direction is -1
        :param color: color of piece
        :param left:How many left on the left side
        :param skipped:the list includes the piece can be skipped
        :param r: row

        :return a direction of all possible moves{( possibleFoothold x,possibleFoothold ,y):(the color of possible overlap piece )}

        '''
        moves = {}
        last_piece = []
        for row in range(start, stop, step):
            if left < 0:
                break

            current = self.board[row][left]
            #found empty place
            if current == 0:
                #met edge of board
                if captured and not last_piece:
                    break
                # do muti-leg
                elif captured:
                    moves[(row, left)] = last_piece + captured
                # has empty place and has captured things, do normal
                else:
                    moves[(row, left)] = last_piece
                #check if can do multi-leg
                if last_piece:
                    if step == -1:
                        minmax_row = max(row-3, 0)
                    else:
                        minmax_row = min(row+3, ROWS)
                    moves.update(self.left_iteration(row+step, minmax_row, step, color, left-1,captured=last_piece))
                    moves.update(self.right_iteration(row+step, minmax_row, step, color, left+1,captured=last_piece))
                break
            # has a same color piece ,break
            elif current.color == color:
                break
            # can jump over but must check next
            else:
                last_piece = [current]

            left -= 1

        return moves
    # do mirrow operation
    def right_iteration(self, start, stop, step, color, right, captured=[]):
        moves = {}
        last_piece = []
        for row in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[row][right]
            if current == 0:
                if captured and not last_piece:
                    break
                elif captured:
                    moves[(row,right)] = last_piece + captured
                else:
                    moves[(row, right)] = last_piece

                if last_piece:
                    if step == -1:
                        minmax_row = max(row-3, 0)
                    else:
                        minmax_row = min(row+3, ROWS)
                    moves.update(self.left_iteration(row+step, minmax_row, step, color, right-1,captured=last_piece))
                    moves.update(self.right_iteration(row+step, minmax_row, step, color, right+1,captured=last_piece))
                break
            elif current.color == color:
                break
            else:
                last_piece = [current]

            right += 1

        return moves

    def evaluate(self):

        #ai is friend lol
        if self.DIFFICULTY ==1:
            return self.red_number - self.blue_number

        #normal
        if self.DIFFICULTY ==2:
            return self.blue_number - self.red_number + (self.blue_kings * 2 - self.red_kings * 2)

        # let more piece to enemies half of board.
        #[downside_red,downside_blue,upside_red,upside_blue/not king ]
        if self.DIFFICULTY ==3:
            pieces_location = self.board_state()
            total = pieces_location[0]+pieces_location[1]+pieces_location[2]+pieces_location[3]
            return ((pieces_location[3] * 5 + pieces_location[1] *7 +self.blue_kings *10)-
                    (pieces_location[0] * 5 + pieces_location[2] *7 +self.red_kings *10))/total



    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        #print(pieces)
        return pieces



    def get_current_state(self,pieces):
        dr,db,ur,ub=0,0,0,0
        for piece in pieces:
            #[downside_red,downside_blue,upside_red,upside_blue] 0 is false
            if piece.king == False:
                if piece.current_state[0] == 1:
                    dr +=1
                if piece.current_state[1] == 1:
                    db +=1
                if piece.current_state[2] == 1:
                    ur +=1
                if piece.current_state[3] == 1:
                    ub +=1

        return [dr,db,ur,ub]



   # player’s and AI’s Pawns ,Kings in their own respective halves
    def board_state(self):
        pieces = []
        pieces_location=[]
        for row in self.board:
            for piece in row:
                if piece != 0 :
                    pieces.append(piece)
        pieces_location = self.get_current_state(pieces)
        return(pieces_location)
