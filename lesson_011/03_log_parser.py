# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#

#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def log_generator():
    with open('events.txt', 'r') as file:
        stat = {}

        for line in file:

            if 'NOK' in line:
                out_log_format = line[1: 17] + line[28:]
                if out_log_format[1:16] in stat:
                    stat[out_log_format[1:16]] += 1
                else:
                    if stat:
                        yield list(stat.items())[0]
                        stat = {}
                        stat[out_log_format[1:16]] = 1
                    else:
                        stat[out_log_format[1:16]] = 1
        if stat:
            yield list(stat.items())[0]


# TODO Долго думал ничего не придумал. Не покидает чувство беспокойства, что код кривой и можно проще.
# TODO Последние две строчки добавлены, потому, что последние данные остаются в словаре. Не догадался, прошу содействия.


grouped_events = log_generator()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
