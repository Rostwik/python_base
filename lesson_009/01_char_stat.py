# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class CountLettersFile:
    total = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        filename = 'empty.txt'
        for filename in zfile.namelist():
            zfile.extract(filename)
        return filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            unzipfile = self.unzip()
            if unzipfile == 'empty.txt':
                print('Архив пустой!')
                return
            else:
                with open(unzipfile, 'r', encoding='cp1251') as file:
                    for line in file:
                        self._collect_in_line(line)

    def _collect_in_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                    self.total += 1
                else:
                    self.stat[char] = 1
                    self.total += 1

    def display_stat(self, list_count):
        print('+{txt:-^18}+'.format(txt='+'))
        print('|{:^8}|{:^9}|'.format('Буква', 'Частота'))
        print('+{txt:-^18}+'.format(txt='+'))
        for char, count in list_count:
            print('|{simbol:^8}|{frequency:^9}|'.format(simbol=char, frequency=count))
        print('+{txt:-^18}+'.format(txt='+'))
        print('|{:^8}|{:^9}|'.format('Итого', self.total))
        print('+{txt:-^18}+'.format(txt='+'))

    def frequency_ascending(self):
        list_count_of_simbols = list(self.stat.items())
        list_count_of_simbols.sort(key=lambda list_count_of_simbols: list_count_of_simbols[1])
        self.display_stat(list_count_of_simbols)

    def alphabetically_ascending(self):
        list_count_of_simbols = sorted(self.stat.items())
        self.display_stat(list_count_of_simbols)

    def alphabetically_descending(self):
        list_count_of_simbols = sorted(self.stat.items(), reverse=True)
        self.display_stat(list_count_of_simbols)


count_of_simbols = CountLettersFile('python_snippets\\voyna-i-mir.txt.zip')

count_of_simbols.collect()
count_of_simbols.alphabetically_ascending()
count_of_simbols.alphabetically_descending()
count_of_simbols.frequency_ascending()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!
