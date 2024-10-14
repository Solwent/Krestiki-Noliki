import os

def restart_program():
    print('Игра завершена. Хотите ли начать заново?')
    do = int(input('Для рестарта введите 1\n'))
    if do == 1:
        os.system("python main.py")