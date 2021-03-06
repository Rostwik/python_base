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


class Logger:

    def __init__(self, filename_in, filename_out):
        self.filename_in = filename_in
        self.filename_out = filename_out
        self.stat = {}

    def reformat(self, last_characters):
        self.stat = {}
        dead_end = 17 - last_characters
        with open(self.filename_in, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    out_log_format = line[1:dead_end]
                    if out_log_format in self.stat:
                        self.stat[out_log_format] += 1
                    else:
                        self.stat[out_log_format] = 1

    def write_data(self):
        with open(self.filename_out, 'w') as file:
            for data, count in self.stat.items():
                file.write(f'[{data}] {count} \n')

    def hour_format(self):
        last_characters = 3
        self.reformat(last_characters)

    def day_format(self):
        last_characters = 6
        self.reformat(last_characters)

    def month_format(self):
        last_characters = 9
        self.reformat(last_characters)

    def year_format(self):
        last_characters = 12
        self.reformat(last_characters)

    def minute_format(self):
        last_characters = 0
        self.reformat(last_characters)


new_data = Logger('events.txt', 'out_events.txt')

new_data.minute_format()
new_data.write_data()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

#зачет!