# -*- coding: utf-8 -*-

class ShotState:

    def __init__(self):
        self.score = 0
        self.score_digit = 0
        self.symbol = ''
        self.total = False

    def run(self):
        pass


class ShotStateOne(ShotState):

    def run(self):
        if self.symbol == '/':
            raise ErrorFormatData("Обратите внимание на spare - фрейм не может начинаться с '/'.")
        if self.symbol.isdigit():
            self.score_digit += int(self.symbol)
        if self.symbol == 'X':
            self.score += 20


class ShotStateTwo(ShotState):

    def run(self):
        if self.symbol == '/':
            self.total = True
        if self.symbol.isdigit():
            self.score_digit += int(self.symbol)


class Frame:

    def __init__(self, state):
        self.score_frame = 0
        self.state = state

    def change_state(self, state):
        self.state = state


class ErrorLenData(Exception):
    pass


class ErrorSumShot(Exception):
    pass


class ErrorFormatData(Exception):
    pass


def get_score(game_result):
    score = 0
    shot_one = ShotStateOne()
    shot_two = ShotStateTwo()
    frame_bowl = Frame(shot_one)

    for shot in game_result:
        if shot not in 'X/123456789-':
            raise ErrorFormatData('Недопустимые символы в данных!')

    game_result = game_result.replace('X', 'XX')

    if len(game_result) % 2:
        raise ErrorLenData('Проверьте данные - неверное количество символов!')

    game_result = [game_result[x:x + 2] for x in range(0, len(game_result), 2)]
    print(game_result)

    for shot in game_result:
        frame_bowl.state.symbol = shot[0]
        frame_bowl.state.run()
        frame_bowl.score_frame += frame_bowl.state.score + frame_bowl.state.score_digit
        frame_bowl.change_state(shot_two)
        frame_bowl.state.symbol = shot[1]
        frame_bowl.state.run()
        if shot_one.score_digit + shot_two.score_digit > 10:
            raise ErrorFormatData('Проверьте, пожалуйста, данные - кеглей всего 10.')
        elif frame_bowl.state.total:
            score += 15
        else:
            score += frame_bowl.score_frame + frame_bowl.state.score + frame_bowl.state.score_digit
        shot_one = ShotStateOne()
        shot_two = ShotStateTwo()
        frame_bowl.change_state(shot_one)
        frame_bowl.score_frame = 0


    print(score)




# for shot in game_result:
#     if shot == '//' or shot[0] == '/':
#         raise ErrorFormatData(
#             "Обратите внимание на spare - не может быть два символа '/' в одном фрейме,"
#             "также фрейм не может начинаться с '/'.")
#     elif shot == 'XX':
#         score += 20
#     elif shot[0].isdigit():
#         if shot[1].isdigit():
#             if int(shot[0]) + int(shot[1]) > 10:
#                 raise ErrorFormatData('Проверьте, пожалуйста, кеглей всего 10.')
#             else:
#                 score += int(shot[0]) + int(shot[1])
#         else:
#             if shot[1] == '/':
#                 score += 15
#             else:
#                 score += int(shot[0])
#     else:
#         if shot[0] == '-':
#             if shot[1].isdigit():
#                 score += int(shot[1])
#             elif shot[1] == '/':
#                 score += 15
