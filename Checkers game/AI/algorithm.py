from copy import deepcopy
from checkers.constants import RED, BLUE






def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move



# algorithm
def alpha_beta(position, depth, max_player, game,alpha,beta):

    if depth == 0 or position.get_winner() != None:
        return position.evaluate(), position,alpha,beta

    if max_player:#AI
        max_evaluation = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = alpha_beta(move, depth-1, False, game,alpha,beta)[0]
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha,max_evaluation)

            if max_evaluation == evaluation:
                best_move = move

            if beta <= alpha:
                break
        return max_evaluation, best_move,alpha,beta
    else:#HUMAN
        min_evaluation = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = alpha_beta(move, depth-1, True, game,alpha,beta)[0]
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta,min_evaluation)

            if min_evaluation == evaluation:
                best_move = move

            if beta <= alpha:
                break
        return min_evaluation, best_move,alpha,beta







def ai_move(piece, move, board, game, capture):
    #move[0] row
    #move[1] column
    board.move(piece, move[0], move[1])
    if capture:
        board.ai_skip(capture)

    return board


def get_all_moves(board, color, game):
    moves = []


    for piece in board.get_all_pieces(color):
        available_moves = board.get_available_moves(piece)
        print(available_moves)
        #,list of piece
        for move, skip in available_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = ai_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

