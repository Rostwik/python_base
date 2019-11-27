# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    exception_dict = {1: IamGodError, 2: DrunkError, 3: CarCrashError, 4: GluttonyError,
                      5: DepressionError, 6: SuicideError}

    karma = randint(1, 7)
    dice = randint(1, 13)
    if dice == 13:
        dice = randint(1, 6)
        raise exception_dict[dice]
    return karma


ENLIGHTENMENT_CARMA_LEVEL = 0

while True:
    try:
        karma = one_day()
        ENLIGHTENMENT_CARMA_LEVEL += karma
        if ENLIGHTENMENT_CARMA_LEVEL >= 777:
            break
    except IamGodError:
        print('Билл думает о вечном.')
    except DrunkError:
        print('Билл напился.')
    except CarCrashError:
        print('Билл гоняет на машине по железнодорожным путям.')
    except GluttonyError:
        print('Билл не боится холестерина.')
    except DepressionError:
        print('Билл не хочет вставать из кроватки.')
    except SuicideError:
        print('Билл опустил тостер в ванну.')
# TODO А как же запись исключений в лог?
# https://goo.gl/JnsDqu
