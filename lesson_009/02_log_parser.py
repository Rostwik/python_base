# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from pprint import pprint


class Loger():

    def __init__(self, filename_in, filename_out):
        self.filename_in = filename_in
        self.filename_out = filename_out
        self.stat = {}

    def reformat(self, a):
        self.stat = {}
        deadend = 17 - a
        with open(self.filename_in, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    out_log_format = line[1:deadend]
                    if out_log_format in self.stat:
                        self.stat[out_log_format] += 1
                    else:
                        self.stat[out_log_format] = 1

    def write_data

    def hh_format(self):

        a = 3
        self.reformat(a)

    def dd_format(self):

        a = 6
        self.reformat(a)

    def mm_format(self):

        a = 9
        self.reformat(a)

    def yyyy_format(self):

        a = 12
        self.reformat(a)


new_data = Loger('events.txt', 'out_events.txt')

new_data.yyyy_format()
pprint(new_data.stat)
new_data.hh_format()
pprint(new_data.stat)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
