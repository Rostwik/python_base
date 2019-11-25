# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class VerificationRegistrationData():

    def __init__(self, inputfile):
        self.datafile = inputfile
        self.out_good_data = []
        self.out_bad_data = []

    def write_data(self, outfile, outdata):
        with open(outfile, 'w') as file:
            for data in outdata:
                file.write(f'{data}\n')

    def str_analysis(self, datastr):

        error1 = ' НЕ присутсвуют все три поля'
        error2 = ' поле имени содержит НЕ только буквы'
        error3 = ' поле емейл НЕ содержит @ и .(точку)'
        error4 = ' поле возраст НЕ является числом от 10 до 99'

        all_three_fields = datastr.split(' ')
        if len(all_three_fields) != 3:
            raise ValueError(datastr[:-1] + error1)
        elif not all_three_fields[0].isalpha():
            raise NotNameError(datastr[:-1] + error2)
        elif '@' not in all_three_fields[1] and '.' not in all_three_fields[1]:
            raise NotEmailError(datastr[:-1] + error3)
        elif not 10 <= int(all_three_fields[2]) <= 99:
            raise ValueError(datastr[:-1] + error4)
        else:
            return datastr[:-1]


myfirstweb = VerificationRegistrationData('registrations.txt')


with open(myfirstweb.datafile, 'r', encoding='cp1251') as file:
    for line in file:
        try:
            myfirstweb.out_good_data += [myfirstweb.str_analysis(line)]
        except (ValueError, NotNameError, NotEmailError) as exp:
            myfirstweb.out_bad_data += exp.args

myfirstweb.write_data('registrations_good.log', myfirstweb.out_good_data)
myfirstweb.write_data('registrations_bad.log', myfirstweb.out_bad_data)


