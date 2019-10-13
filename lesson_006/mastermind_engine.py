# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

import random

make_secret_number = ''


def make_number():
    global make_secret_number
    make_secret_number = ''
    i = 3
    make_secret_number = str(random.randint(1, 9))
    while i != 0:
        random_digit = random.randint(0, 9)
        if str(random_digit) not in make_secret_number:
            make_secret_number = make_secret_number + str(random_digit)
            i -= 1
    return make_secret_number


def check_number(user_number):
    hint = {'bulls': 0, 'cows': 0}
    for digit in range(4):
        if user_number[digit] in make_secret_number:
            if user_number[digit] == make_secret_number[digit]:
                hint['bulls'] += 1
            else:
                hint['cows'] += 1
    return hint


def verify_user_number(user_number):
    if not user_number.isdigit():
        print('Вы ввели текстовую информацию')
        return False
    else:
        if len(user_number) != 4:
            print('Введена цифра несоответствующей разрядности')
            return False
        else:
            if user_number[0] == '0':
                print('Первая цифра не должна быть нулем')
                return False
            else:
                return True
