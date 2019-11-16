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
        self.filename = filename_in
        self.filename = filename_out
        stat = {}

    def counter(self, sign):
        pass


stat = {}


with open('events.txt', 'r') as file:
    for line in file:
        year = line[1:5]
        month = line[6:8]
        day = line[9:11]
        hour = line[12:14]
        minute = line[15:17]
        if 'NOK' in line:
            if year not in stat:
                stat[year] = {}
                if month not in stat[year]:
                    stat[year][month] = {}
                    if day not in stat[year][month]:
                        stat[year][month][day] = []
                        stat[year][month][day].append([hour, minute])

            else:
                if month not in stat[year]:
                    stat[year][month] = {}
                    if day not in stat[year][month]:
                        stat[year][month][day] = []
                        stat[year][month][day].append([hour, minute])

                else:
                    if day not in stat[year][month]:
                        stat[year][month][day] = []
                        stat[year][month][day].append([hour, minute])

                    else:
                        stat[year][month][day].append([hour, minute])

pprint(stat)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
