board_size = int(input('Введите желаемый размер поля\n'))
board_numbers = board_size ** 2

# Игровое поле
def draw_board(board_size):
      # общее количество ячеек
    board = [i + 1 for i in range(board_numbers)]  # заполняем доску числами от 1 до board_numbers
    
    print(' ' + '____ ' * board_size)  # верхняя граница
    for i in range(board_size):
        # левый край и ячейки
        row = '|'
        for j in range(board_size):
            row += f' {board[i * board_size + j]:<2} |'  # форматирование для каждого элемента
        print(row)  # вывод строки
        print('|' + '----|' * board_size)  # границы ячеек


def game_step():
    
    pass


def start_game():
    current_player = 'X'
    step = 1
    
    draw_board(board_size)

    while step<=board_numbers:
        index = input('Ход игрока ' + 
                      current_player + 
                      ' Введите номер поля (0 - выход):')


print('Игра "Крестики-Нолики запущена!"')
start_game()