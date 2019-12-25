# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-


import os
import multiprocessing
from pprint import pprint

import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.monotonic()

        result = func(*args, **kwargs)

        ended_at = time.monotonic()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


def file_path(data_directory):
    list_file_paths = []
    for tup in os.walk(data_directory):
        for file in tup[2]:
            if 'csv' in file:
                filepath = os.path.join(data_directory, file)
                list_file_paths.append(filepath)
    return list_file_paths


def display_result(collector):
    volatility = []
    volatility_0 = []

    while not collector.empty():
        data = collector.get()
        if data[0]:
            if not data[1]:
                volatility_0.append(data[0])
            else:
                volatility.append([data[0], data[1]])
    volatility.sort(key=lambda list_vol: list_vol[1], reverse=True)

    print('Максимальная волатильность:')
    for index in volatility[0:3]:
        print(f'     {index[0]:} - {index[1]:3.2f} %')
    print('Минимальная волатильность:')
    for index in volatility[:-4:-1][::-1]:
        print(f'     {index[0]:} - {index[1]:3.2f} %')
    print('Нулевая волатильность:')
    volatility_0.sort()
    print('    ', end=' ')
    print(', '.join(volatility_0))


class Volatility(multiprocessing.Process):

    def __init__(self, filepath, collector):
        super().__init__()
        self.minmax_list = []
        self.volatility = 0
        self.secid = ''
        self.filepath = filepath
        self.collector = collector

    def collect_data_from_files(self):
        try:
            with open(self.filepath, 'r') as tiker_file:
                tiker_file.readline()
                for line in tiker_file:
                    secid, tradetime, price, quantity = line.split(',')
                    self.minmax_list.append(float(price))

            self.secid = secid
        except UnboundLocalError:
            print(f'Проблема с файлом {self.filepath}.')



    def run(self):
        self.collect_data_from_files()
        if self.secid:
            max_vol = max(self.minmax_list)
            min_vol = min(self.minmax_list)
            average_price = (max_vol + min_vol) / 2
            delta = max_vol - min_vol
            self.volatility = (delta / average_price) * 100
            self.collector.put([self.secid, self.volatility])


@time_track
def main():
    list_file_paths = file_path('trades')
    collector = multiprocessing.Queue()
    tikers = [Volatility(filepath=filepath, collector=collector) for filepath in list_file_paths]

    for tiker in tikers:
        tiker.start()
    for tiker in tikers:
        tiker.join()

    display_result(collector)


if __name__ == '__main__':
    main()

