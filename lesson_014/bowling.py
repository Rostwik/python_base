# -*- coding: utf-8 -*-

class ErrorLenData(Exception):
    pass


class ErrorSumShot(Exception):
    pass


class ErrorFormatData(Exception):
    pass


def get_score(game_result):
    score = 0
    for shot in game_result:
        if shot not in 'X/123456789-':
            raise ErrorFormatData('Недопустимые символы в данных!')

    game_result = game_result.replace('X', 'XX')

    if len(game_result) // 2 != 10:
        raise ErrorLenData('Проверьте данные - неверное количество символов!')

    game_result = [game_result[x:x + 2] for x in range(0, len(game_result), 2)]
    print(game_result)

    for shot in game_result:
        if shot == '//' or shot[0] == '/':
            raise ErrorFormatData(
                "Обратите внимание на spare - не может быть два символа '/' в одном фрейме,"
                "также фрейм не может начинаться с '/'.")
        elif shot == 'XX':
            score += 20
        elif shot[0].isdigit():
            if shot[1].isdigit():
                if int(shot[0]) + int(shot[1]) > 10:
                    raise ErrorFormatData('Проверьте, пожалуйста, кеглей всего 10.')
                else:
                    score += int(shot[0]) + int(shot[1])
            else:
                if shot[1] == '/':
                    score += 15
                else:
                    score += int(shot[0])
        else:
            if shot[0] == '-':
                if shot[1].isdigit():
                    score += int(shot[1])
                elif shot[1] == '/':
                    score += 15
    print(score)

get_score('-/37X1111111111282/')
