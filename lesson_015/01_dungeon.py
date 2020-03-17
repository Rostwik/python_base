# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет только две локации и не будет мобов
# (то есть в коренном json-объекте содержится список, содержащий только два json-объекта и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#

#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...

# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890


import datetime
import re
import json
from decimal import *
import csv

from termcolor import cprint

remaining_time = '123456.0987654321'


# если изначально не писать число в виде строки - теряется точность!

class Journey:

    def __init__(self, remaining_time, map):
        """
        Класс Путешествие. Реализует игровую логику.

        :param remaining_time: Время, отведенное для прохождение квеста.
        :param map: JSON файл с монстарми и локациями.
        :param time_spent: затраченное время на прохождение

        """
        self.location = None
        self.list_of_location = []
        self.experience = 0
        self.start_time = Decimal(remaining_time)
        self.time_spent = 0
        self.map = map

    def calculation_time_and_experience(self, data, flag=True):
        """
        Расчет времени и опыта

        :param data: Передается строка, в зависимости от выбора "Локация" или "Монстр"
        :param flag: Если "Локация", передается False, чтобы учитывать только время
        :return:

        """
        exp = re.search(r'(exp)(\d+)', data)
        time = re.search(r'(tm)(\d+)', data)

        if flag:
            self.experience += Decimal(exp[2])
            self.time_spent += Decimal(time[2])
        else:
            self.time_spent += Decimal(time[2])

        return

    def csv_result_file(self):
        """
        Записываем результат игры.
        :return: возвращаем признак окончания игры
        """
        field_names = ['current_location', 'current_experience', 'current_date']

        with open('dungeon.csv', 'a', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
            writer.writerow({'current_location': self.location, 'current_experience': self.experience,
                             'current_date': datetime.datetime.now()})
        return False

    def moves(self):
        exit = True
        self.load_map()

        while exit:

            where_to_go = {}
            whom_to_kill = []

            # Обновляем текущее окружение.
            deadline, environment = self.update_current_position()

            # Проверка окончания игры.
            if deadline <= 0:
                print('Время вышло. Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! RIP.')
                self.csv_result_file()
                break
            elif 'Hatch' in self.location:
                print('Вы видите спасительный люк! Вы пробуете его открыть.. ')
                if self.experience < 280:
                    print('О Боже! Вы мало качались на мобах и Вам не хватает сил..')
                else:
                    print('Вы спасены! Свобода! Вы победитель по жизни, и Вас ждут новые испытания!')
                self.csv_result_file()
                break

            print(f'У вас {self.experience} опыта и осталось {deadline} секунд до наводнения')
            print(f'Прошло времени {str(datetime.timedelta(seconds=float(self.time_spent)))}')

            # Осматриваем пещеру.
            print('Внутри вы видите:')
            self.look_around(environment, where_to_go, whom_to_kill)

            # Выбор пользователя, что делаем дальше.
            exit = self.choice(whom_to_kill, where_to_go)

        self.end_or_new_game()

    def end_or_new_game(self):
        while True:

            choice = input('Текущая игра завершена. Желаете начать новую? (y/n)')

            if choice == 'y' and len(choice) == 1:
                self.location = None
                self.list_of_location = []
                self.experience = 0
                self.start_time = Decimal(remaining_time)
                self.time_spent = 0
                self.moves()
                break
            elif choice == 'n' and len(choice) == 1:
                print('Всего доброго! Приходите еще.')
                break
            else:
                print('Введен неверный символ. Попробуйте еще раз.')

    def choice(self, whom_to_kill, where_to_go):
        """
        Осознанный выбор пользователя.

        :param whom_to_kill: список монстров на локации
        :param where_to_go: список выходов из пещеры
        :return:
        """

        action_options = ['1', '2', '3']
        while True:

            cprint('Выберите действие: ', attrs=['underline'])
            if whom_to_kill:
                print('1.Атаковать монстра')
            if where_to_go:
                print('2.Перейти в другую локацию')
            print('3.Сдаться и выйти из игры')

            cprint('Что Вы выбрали?', 'magenta')
            choice = input()

            if choice in action_options:
                if choice == '3':  # выход из игры
                    return self.csv_result_file()

                elif choice == '2':  # выбираем "переходим на другую локацию"
                    cprint('Выберите локацию: ', attrs=['underline'])
                    for number, location in where_to_go.items():
                        cprint(f'Нажми {number} для локации {list(location.items())[0][0]}', attrs=['blink'])
                    cprint('Что Вы выбрали?', 'magenta')
                    while True:
                        choice = input()  # выбираем локацию из списка
                        if choice.isdigit():
                            if int(choice) in where_to_go.keys():
                                self.list_of_location = where_to_go[int(choice)]
                                self.calculation_time_and_experience(list(self.list_of_location)[0], False)
                                break
                        cprint('Вы ввели неверный символ, пожалуйста, попробуйте еще раз!', 'red')
                    return True

                elif choice == '1':  # выбираем "атаковать монстра"
                    print('Выбери цель: ')
                    for number, monstr in enumerate(whom_to_kill):
                        print(f'Нажми {number}, чтобы сразиться с {monstr}')
                    while True:
                        choice = input()  # выбираем монстра из списка для атаки
                        if choice.isdigit():
                            if int(choice) in list(range(len(whom_to_kill))):
                                self.calculation_time_and_experience(whom_to_kill.pop(int(choice)))
                                break
                        cprint('Вы ввели неверный символ, пожалуйста, попробуйте еще раз!', 'red')

            else:
                cprint('Вы ввели неверный символ, пожалуйста, попробуйте еще раз!', 'red')
        return True

    def look_around(self, environment, where_to_go, whom_to_kill):
        for member, j in enumerate(environment):
            if 'exp' in j:
                whom_to_kill.append(j)
                print(f'- Монстра {j}')
            else:
                where_to_go[member] = j
                print(f'- Вход в локацию: {list(j.items())[0][0]}')

    def update_current_position(self):

        location, environment = list(self.list_of_location.items())[0]
        print(f'Вы находитесь в {location}')
        self.location = location
        deadline = self.start_time - self.time_spent
        return deadline, environment

    def load_map(self):

        with open(self.map, "r") as json_file:
            self.list_of_location = json.load(json_file)


journey = Journey(remaining_time, 'rpg.json')
journey.moves()

# Учитывая время и опыт, не забывайте о точности вычислений!
