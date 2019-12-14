# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.counter = 0
        self.interval = n
        self.prime_numbers = []

    def __iter__(self):
        self.counter = 0
        self.prime_numbers = []

        return self

    def __next__(self):
        while True:
            self.counter += 1
            if self.counter >= self.interval:
                raise StopIteration()
            else:
                number = 1 + self.counter
                for prime in self.prime_numbers:
                    if number % prime == 0:
                        break
                else:
                    self.prime_numbers.append(number)
                    return number


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True

def armstrong_number(prime_number):
    narcissistic_number = 0
    degree = len(str(prime_number))
    str_number = str(prime_number)
    narcissistic_number = sum(list(map(lambda x, xx=degree: int(x) ** xx, str_number)))
    if prime_number == narcissistic_number:
        return True





def happy_filter(prime_number):
    extra_sign = 0
    str_number = (str(prime_number))
    if len(str(prime_number)) == 1:
        return
    if len(str_number) % 2 != 0:
        extra_sign = 1
    number_of_signs = int(((len(str_number)) - extra_sign) / 2)
    left_part = str_number[:number_of_signs]
    right_part = str_number[-number_of_signs:]
    if sum(list(map(int, left_part))) == sum(list(map(int, right_part))):
        return True


def palindrome_filter(prime_number):
    extra_sign = 0
    str_number = (str(prime_number))
    if len(str(prime_number)) == 1:
        return
    if len(str_number) % 2 != 0:
        extra_sign = 1
    number_of_signs = int(((len(str_number)) - extra_sign) / 2)
    left_part = str_number[:number_of_signs]
    right_part = str_number[-number_of_signs:][::-1]  # TODO: подскажите, пожалуйста, а здесь можно проще?
    if left_part == right_part:
        return True


def prime_numbers_generator(n, func):
    counter = 0
    interval = n
    prime_numbers = []
    while True:
        counter += 1
        if counter >= interval:
            break
        else:
            number = 1 + counter
            for prime in prime_numbers:
                if number % prime == 0:
                    break
            else:
                prime_numbers.append(number)
                if func(number):
                    yield number


for number in prime_numbers_generator(n=10000, func=armstrong_number):
    print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
