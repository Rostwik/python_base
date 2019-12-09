# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
# на консоли должно появится что-то вроде
# [2018-05-17 01:57] 1234

def read_file_data(file):
    with open(file, 'r') as file:
        for line in file:
            yield line


def log_generator(file):

        stat = {}
        file_data = read_file_data(file)

        for line in file_data:

            if 'NOK' in line:
                out_log_format = line[1:17]
                if out_log_format in stat:
                    stat[out_log_format] += 1
                else:
                    if stat:
                        yield list(stat.items())[0]
                        stat = {}
                        stat[out_log_format] = 1
                    else:
                        stat[out_log_format] = 1
        if stat:
            yield list(stat.items())[0]


# Долго думал ничего не придумал. Не покидает чувство беспокойства, что код кривой и можно проще.
# Последние две строчки добавлены, потому, что последние данные остаются в словаре. Не догадался, прошу содействия.


grouped_events = log_generator('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
