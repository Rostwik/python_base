# -*- coding: utf-8 -*-


import os
from pprint import pprint

import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class Volatility:

    def __init__(self, input_dir):
        self.data_directory = input_dir
        self.list_file_paths = []
        self.volatility = []
        self.volatility_0 = []
        self.minmax_list = []

    def display_result(self):
        print('Максимальная волатильность:')
        for index in self.volatility[0:3]:
            print(f'     {index[0]:} - {index[1]:3.2f} %')
        print('Минимальная волатильность:')
        for index in self.volatility[:-4:-1][::-1]:
            print(f'     {index[0]:} - {index[1]:3.2f} %')
        print('Нулевая волатильность:')
        self.volatility_0.sort()
        print('    ', end=' ')
        print(', '.join(self.volatility_0))

    def collect_data_from_files(self, file):
        with open(file, 'r') as tiker_file:
            tiker_file.readline()
            for line in tiker_file:
                secid, tradetime, price, quantity = line.split(',')
                self.minmax_list.append(float(price))
        return secid

    def file_path(self):
        for tup in os.walk(self.data_directory):
            for file in tup[2]:
                if 'csv' in file:
                    filepath = os.path.join(self.data_directory, file)
                    self.list_file_paths.append(filepath)

    def run(self):
        self.file_path()
        for file in self.list_file_paths:
            self.minmax_list = []
            secid = self.collect_data_from_files(file)
            max_vol = max(self.minmax_list)
            min_vol = min(self.minmax_list)
            average_price = (max_vol + min_vol) / 2
            delta = max_vol - min_vol
            volatility = (delta / average_price) * 100
            if not volatility:
                self.volatility_0.append(secid)
            else:
                self.volatility.append([secid, volatility])
        self.volatility.sort(key=lambda list_vol: list_vol[1], reverse=True)
        self.display_result()


@time_track
def main():
    success = Volatility('trades')
    success.run()


if __name__ == '__main__':
    main()
