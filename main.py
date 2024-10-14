from win import check_win

board_size = int(input('Введите желаемый размер поля\n'))
board_numbers = board_size ** 2
board = [i + 1 for i in range(board_numbers)]

# Игровое поле
def draw_board(board_size):  
    print(' ' + '____ ' * board_size)  # верхняя граница
    for i in range(board_size):
        # левый край и ячейки
        row = '|'
        for j in range(board_size):
            row += f' {board[i * board_size + j]:<2} |'  # форматирование для каждого элемента
        print(row)  # вывод строки
        print('|' + '----|' * board_size)  # границы ячеек


def game_step():
    current_player = 'X'
    step = 1

    while step<=board_numbers and (check_win(board,board_size) == False):
        index = int(input('Ход игрока ' + 
                      current_player + 
                      ' Введите номер поля (0 - выход):'))
        if index == 0:
            break
        step += 1
        board[index-1] = current_player

        if (current_player == 'X'):
            current_player = 'O'
        else:
            current_player = 'X'
        
        draw_board(board_size)
    if check_win(board,board_size) != False:
        print('Выиграл игрок' + check_win(board,board_size))
    

def start_game():
    
    draw_board(board_size)
    game_step()

    
print('Игра "Крестики-Нолики запущена!"')
start_game()