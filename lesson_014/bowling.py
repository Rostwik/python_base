# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class ShotState(metaclass=ABCMeta):

    def __init__(self):
        self.symbol = ''

    def run(self):
        result = 0
        if self.symbol == 'X':
            result = self.strike()
        elif self.symbol == '/':
            result = self.spare()
        elif self.symbol.isdigit():
            result = int(self.symbol)
        return result

    @abstractmethod
    def strike(self):
        pass

    @abstractmethod
    def spare(self):
        pass


class ShotStateOne(ShotState):

    def strike(self):
        return 20

    def spare(self):
        raise ErrorFormatData("Обратите внимание на spare - фрейм не может начинаться с '/'.")


class ShotStateTwo(ShotState):

    def strike(self):
        return 0

    def spare(self):
        return 15


class Frame:

    def __init__(self, state):
        self.score_frame = 0
        self.state = state

    def change_state(self, state):
        self.state = state


def state_machine(shot, frame, state1, state2):
    frame.state.symbol = shot[0]
    score1 = frame.state.run()
    frame.change_state(state2)

    frame.state.symbol = shot[1]
    score2 = frame.state.run()
    frame.change_state(state1)

    if score1 == 20:
        return 20
    elif score2 == 15:
        return 15
    elif (score2 + score1) > 10:
        raise ErrorFormatData('Проверьте, пожалуйста, данные фреймов - кеглей всего 10.')
    else:
        return score2 + score1


class ErrorLenData(Exception):
    pass


class ErrorSumShot(Exception):
    pass


class ErrorFormatData(Exception):
    pass


def get_score(game_result):
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

    for shot in game_result:
        frame_bowl.score_frame += state_machine(shot, frame_bowl, shot_one, shot_two)

    return frame_bowl.score_frame
