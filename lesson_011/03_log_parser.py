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
                if out_log_format[1:16] in stat:  # TODO Тут теряется первая цифра от года
                    # TODO Если здесь и далее используется out_log_format[1:16]
                    # TODO Почему бы сразу и не вырезать нужную подстроку?
                    stat[out_log_format[1:16]] += 1
                else:
                    if stat:
                        yield list(stat.items())[0]
                        stat = {}
                        stat[out_log_format[1:16]] = 1
                    else:
                        stat[out_log_format[1:16]] = 1
        if stat:  # TODO Последние строки остаются, потому что только одно событие происходит в эту минуту
            # TODO А данных по следующей минуте нет
            yield list(stat.items())[0]


# Долго думал ничего не придумал. Не покидает чувство беспокойства, что код кривой и можно проще.
# TODO Может быть и можно, но и ваш вариант неплох
# TODO Можно подумать о разделении на пару функций (одна для чтения файла, другая для парсинга)
# Последние две строчки добавлены, потому, что последние данные остаются в словаре. Не догадался, прошу содействия.


grouped_events = log_generator()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
