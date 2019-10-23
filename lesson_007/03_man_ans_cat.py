# -*- coding: utf-8 -*-

from random import randint, choice


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
# TODO И у кота и у человека в методах не хватает проверок на наличие ресурсов
# TODO Деньги могут тратиться даже тогда, когда их нет
# TODO Еда съедается вне зависимости от её наличия
# TODO Нужно внести правки (кучу if/else конструкций :))
class Cat:
    def __init__(self):
        self.satiety = 0
        self.house = None
        self.nickname = None

    def sleep(self):
        self.satiety -= 10
        print('Кот храпит!')

    def eat(self):
        self.satiety += 20
        self.house.cat_food -= 10  # TODO Что же делать коту, если дома нет? Вызывать ошибку AttributeError!
        print('Котик чавкает!')

    def tear_wallpaper(self):
        self.satiety -= 10
        self.house.mud += 5  # TODO И тут, бездомный котик не найдёт свои обои
        print('Кот элегантно спускается вниз по новеньким обоям...')

    def status(self):
        print('Сытость кота', self.satiety)

    def act(self):

        if self.satiety < 20:
            self.eat()
        elif self.satiety < 40:
            self.sleep()
        else:
            self.tear_wallpaper()
        dice = randint(1, 6)
        if dice in [1, 3]:
            self.eat()


class Human:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.satiety = 30
        self.money = 300
        print('Меня зовут', self.name, 'У меня нет крыши над головой :(')

    def buy_house(self, house):
        self.house = house
        print('Я купил дом, ура!')

    def shelter_a_pet(self, other, nickname):
        other.house = self.house
        other.nickname = nickname
        print('Я приютил котика по имени', nickname)

    def buy_cat_food(self):
        self.house.cat_food += 50
        self.money -= 50
        print('Котику нечего кушать, надо сходить в Пятерочку, я знаю там сегодня акция на Шебу!')

    def buy_food(self):
        self.house.food += 50
        self.money -= 70
        print('В холодильнике пусто, схожу в магазин!')

    def clean_the_house(self):
        self.house.mud -= 100
        self.satiety -= 20
        print('Опять кот все разбросал :(, убираю!')

    def work(self):
        self.money += 150
        print('Программа сама себя не напишет! Доделаю проект, авось заплатят сразу.')

    def eat(self):
        self.satiety += 20

    def status(self):
        print('Моя сытость:', self.satiety, 'Денег у меня:', self.money, 'В доме грязно на:', self.house.mud)

    def act(self):
        if self.house.food < 100:
            self.buy_food()
        elif self.house.cat_food < 80:
            self.buy_cat_food()
        elif self.house.mud > 120:
            self.clean_the_house()
        elif self.money < 100:
            self.work()
        elif self.satiety < 40:
            self.eat()


class House:
    streets = ['Komsomolskaya', 'Sovetskaya', 'Pionerskaya', 'Lelinskaya']

    def __init__(self):
        self.house_street = choice(House.streets)
        self.food = 40
        self.cat_food = 0
        self.mud = 0


my_house = House()
good_person = Human('Вова')
good_person.buy_house(my_house)
kitten = Cat()
good_person.shelter_a_pet(kitten, 'Persik')

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    kitten.act()
    good_person.act()

    print('--- в конце дня ---')
    kitten.status()
    good_person.status()
    if kitten.satiety < 0:
        print('Котик умер (((((((((')
        break

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
