import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    
    return min_value <= value <= max_value
    
    

def game_board_full(game_board):
    """ (str) -> bool
    
    Return True if and only if there are no EMPTY cells in game_board.
    
    >>> game_board_full('XOOXOXXOO')
    True
    >>> game_board_full('XOOX-XO--')
    False
    """
    
    if EMPTY in game_board:
        return False
    else:
        return True
    


def get_board_size(game_board):
    """ (str) -> int
    
    Return the length of each side of the square game_board.
    
    >>> get_board_size('OOXOXOXXO')
    3
    >>> get_board_size('X-OO')
    2
    """
    
    board_size = (len(str(game_board))) ** (1/2)
    return int(board_size)



def make_empty_board(board_size):
    """ (int) -> str
    
    Precondition: 1 <= board_size <= 9
    
    Return game_board, which side length is set with board_size, only with EMPTY
    characters.
    
    >>> make_empty_board(3)
    '---------'
    >>> make_empty_board(2)
    '----'
    """
    
    game_board = board_size ** 2 * EMPTY
    return game_board



def get_position(row_index, col_index, board_size):
    """ (int, int, int) -> int
    
    Precondition: row_index <= board_size and col_index <= board_size
    
    Return the position of character in game_board of given board_size set by 
    row_index and col_index.
    
    >>> get_position(2, 1, 3)
    3
    >>> get_position(4, 2, 4)
    13
    """ 
    
    str_index = (row_index - 1) * board_size + col_index - 1
    return str_index 



def make_move (player_symbol, row_index, col_index, game_board):
    """ (str, int, int, str) -> str
    
    Precondition: row_index <= board_size and col_index <= board_size
    
    Return new game_board with player_symbol replaced instead of EMPTY cell set
    by row_index and col_index.
    
    >>>make_move ('X', 3, 2, 'XOO-XXO--X')
    'XOO-XXOX-X'
    >>>make_move ('O', 1, 2, 'X---')
    'XO--'
    """
    
    board_size = get_board_size(game_board)
    str_index = get_position(row_index, col_index, board_size)
    return game_board[0:str_index] + player_symbol + game_board[str_index+1:]



def extract_line (game_board, direction, row_or_column_indices):
    """ (str, str, int) -> str
    
    Precondition: if direction == 'down_diagonal' or direction == 'up_diagonal'
    the value of row_or_column_indices should not be used
    
    Return the combination of characters of gameboard, according to given 
    row_or_column_indices and direction.
    
    >>>extract_line ('XXO-', 'across', 1)
    'XX'
    >>>extract_line ('XXO-XXOX-', 'down', 2)
    'XXX'
    >>>extract_line ('OOX-XOXO-', 'up_diagonal', 5)
    'XXX'
    >>>extract_line ('OX-O', 'down_diagonal', 13)
    'OO'
    """
    
    if direction == 'across':
        return game_board[row_or_column_indices * get_board_size(game_board) \
                          - get_board_size(game_board):row_or_column_indices *\
                          get_board_size(game_board)] 
    elif direction == 'down':
        return game_board[row_or_column_indices - 1::get_board_size(game_board)]
    elif direction == 'down_diagonal':
        return game_board[::get_board_size(game_board)+1]
    else: 
        return game_board[get_board_size(game_board)**2 -\
                          get_board_size(game_board):get_board_size(game_board)\
                          - 2: -(get_board_size(game_board)-1)]
