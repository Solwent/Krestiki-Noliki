# Игровое поле
def draw_board(board_size):
    board_numbers = board_size ** 2  # общее количество ячеек
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
    board_size = int(input('Введите желаемый размер поля\n'))
    draw_board(board_size)
    pass

print('Игра "Крестики-Нолики запущена!"')
start_game()