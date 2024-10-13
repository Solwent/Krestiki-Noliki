from keyboard import *
import main
from draw import *
from win import *

def restart():
    print('Игра завершена. Хотите ли начать заново?')
    do = input('Для рестарта введите 1')
    if do == 1:
        restart(main)