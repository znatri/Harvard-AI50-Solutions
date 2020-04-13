"""
Tic Tac Toe Player
"""

import math
import copy

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
    # count 'x' and 'y' in list
    # compare both 
    # whichever is less plays next move
    
    count_x = 0
    count_o = 0

    for row in board:
        count_x += row.count("X") # count number of X in that row
        count_o += row.count("O") # count number of O in that row 
    
    # print(f'X: {count_x}')
    # print(f'O: {count_o}')

    if count_x > count_o:
        return "O"
    elif not terminal(board) and count_x == count_o:
        return "X"
    else:
        return None

# sampleBoard = [[EMPTY, EMPTY, O],[EMPTY, O, O],[EMPTY, X, X]]
# print(player(sampleBoard))

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set() # unordered list (cant call an element using index)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action = (i, j)
                actions.add(action)
    return actions

# sampleBoard = [[EMPTY, EMPTY, O],[EMPTY, O, O],[EMPTY, X, X]]
# print(actions(sampleBoard))


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if board is not terminal board
    if terminal(board):
        raise ValueError("Game is over.")
    # Check if action is possible
    elif action not in actions(board):
        raise ValueError("Invalid move.")
    # Play the turn
    else:
        # Make a copy of the board
        result = copy.deepcopy(board)

        # See which player's turn it is
        playerTurn = player(board)

        # Assign action coordinates
        (i, j) = action

        # Make the move on board
        result[i][j] = playerTurn

        # Return result
        return result
    
# sampleBoard = [[EMPTY, EMPTY, O],[EMPTY, O, O],[EMPTY, X, X]]
# print(result(sampleBoard, (0, 1)))


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # win_boards = [
    #     [[P, , ], [P, , ], [P, , ]],
    #     [[ ,P, ], [ ,P, ], [ ,P, ]],
    #     [[ , ,P], [ , ,P], [ , ,P]],
    #     [[P,P,P], [ , , ], [ , , ]],
    #     [[ , , ], [P,P,P], [ , , ]],
    #     [[ , , ], [ , , ], [P,P,P]],
    #     [[ , ,P], [ ,P, ], [P, , ]],
    #     [[P, , ], [ ,P, ], [ , ,P]]
    # ]

    # Consider all cases 
    # Note to self: Update and try using loops instead of so many if commands
    if board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == 'X':
            return 'X'
        else:
            return 'O'
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == 'X':
            return 'X'
        else:
            return 'O'
    else: 
        return None

# sampleBoard = [[EMPTY, EMPTY, O],[EMPTY, X, O],[EMPTY, X, O]]
# print(winner(sampleBoard))

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True # someone won
    
    for row in board:
        for cell in row:
            if cell == None:
                return False # match not over
    return True # both tie

# sampleBoard = [[X, O, X],[O, O, X],[X, X, O]]
# print(terminal(sampleBoard))

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == "X":
        return 1 # x won 
    elif win == "O":
        return -1 # O won
    else:
        return 0 # terminal case

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)

    # If empty board is provided as input, return corner.
    if board == [[EMPTY]*3]*3:
        return (0,0)

    if p == X:
        v = float("-inf")
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                selected_action = action
    elif p == O:
        v = float("inf")
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                selected_action = action

    return selected_action
    
def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v
