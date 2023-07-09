"""
Tic Tac Toe Player
"""

import math

# Problem specification allows the use deepcopy
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx = 0
    county = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == X:
                countx += 1
            elif board[r][c] == O:
                county += 1
    if countx > county:
        return O    
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    for r in range(3):
        for c in  range(3):
            if board[r][c] == EMPTY:
                ans.add((r, c))
    return ans

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Checking if valid move or not
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError('The specified move is impossible')
    
    # Problem specification allows the use of deepcopy
    newboard = deepcopy(board)
    # Determine whose turn it is to move
    turn = player(board)
    # Place the corresponding symbol
    newboard[action[0]][action[1]] = turn
    
    return newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for r in range(3):

        # Checking Rows
        if board[r][0] == O and board[r][1] == O and board[r][2] == O:
            return O
        if board[r][0] == X and board[r][1] == X and board[r][2] == X:
            return X
        
        #Checking Cols
        if board[0][r] == O and board[1][r] == O and board[2][r] == O:
            return O
        if board[0][r] == X and board[1][r] == X and board[2][r] == X:
            return X
        
    # Checking diagonals
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    
    # Checked every winning state possible by now
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        # Someone has won
        return True
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                # Nobody has won AND there are more valid moves possible
                return False
    # No square is left empty and hence no moves are now possible
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ans = winner(board)
    if ans == None:
        # Since terminal state has been reacher, if there is no winner it means that the game is a tie
        return 0
    elif ans == X:
        return 1
    elif ans == O:
        return -1

# Returns utility of the current board if both players play optimally 
def getutil(board):
    if terminal(board):
        return utility(board)    

    moves = actions(board)
    utils = []

    turn = player(board)

    for move in moves:
        newboard = result(board, move)
        newutil = getutil(newboard)
        utils.append(newutil)
        if turn == O and newutil == -1:
            # Cannot do better, so pointless to explore other options
            break
        if turn == X and newutil == 1:
            # Cannot do better, so pointless to explore other options
            break
    
    utils.sort()
    if turn == O:
        return utils[0]
    else:
        utils.reverse()
        return utils[0]  

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    turn = player(board)
    if turn == X:
        # For X player, his goal is to maximize the score
        best = -10
    else:
        # For O player, his goal is to minimize the score
        best = 10

    bestmove = (0, 0)
    moves = actions(board)
    for move in moves:
        newboard = result(board, move)
        currutil = getutil(newboard)
        if turn == X:
            if currutil > best:
                best = currutil
                bestmove = move
        else:
            if currutil < best:
                best = currutil
                bestmove = move
    
    return bestmove