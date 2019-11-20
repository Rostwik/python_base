# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Sorter():

    def __init__(self, input_dir, output_dir):
        self.start_dir = input_dir
        self.end_dir = output_dir

    def create_dir_copy_into_by_time(self):
        for dirpath, dirnames, filenames in os.walk(self.start_dir):

            for file in filenames:

                full_file_path = os.path.join(dirpath, file)
                file_time = time.gmtime(os.path.getmtime(full_file_path))
                result_year_dir = os.path.join(self.end_dir, str(file_time[0]))
                result_month_dir = os.path.join(result_year_dir, str(file_time[1]))
                if not os.path.isdir(result_year_dir):
                    os.makedirs(os.path.join(result_year_dir))
                if not os.path.isdir(result_month_dir):
                    os.makedirs(os.path.join(result_month_dir))

                shutil.copy2(full_file_path, result_month_dir)


fotoalbum = Sorter('icons',
                   'icons_by_year')

fotoalbum.create_dir_copy_into_by_time()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!
