def check_win(board,board_size):
    two_board = [board[i * board_size:(i + 1) * board_size] for i in range(board_size)]  # Преобразуем в двумерный массив

    # Проверка строк и столбцов
    for i in range(board_size):
        if all(cell == 'X' for cell in two_board[i]):
            return 'X'
        if all(cell == 'O' for cell in two_board[i]):
            return 'O'
        if all(cell == 'X' for cell in [two_board[j][i] for j in range(board_size)]):
            return 'X'
        if all(cell == 'O' for cell in [two_board[j][i] for j in range(board_size)]):
            return 'O'
    
    # Проверка диагоналей
    if all(two_board[i][i] == 'X' for i in range(board_size)):
        return 'X'
    if all(two_board[i][i] == 'O' for i in range(board_size)):
        return 'O'
    if all(two_board[i][board_size - 1 - i] == 'X' for i in range(board_size)):
        return 'X'
    if all(two_board[i][board_size - 1 - i] == 'O' for i in range(board_size)):
        return 'O'
    
    return False
