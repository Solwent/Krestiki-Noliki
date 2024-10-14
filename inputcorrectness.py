def inputnum(board_size):
    pass


def inputcor(index, board_numbers, board):
    if (index < 1 or index > board_numbers or board[index-1] in ('X', 'O')):
        return False
    return True