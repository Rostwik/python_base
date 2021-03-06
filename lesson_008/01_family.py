# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class Mammal:
    def __init__(self, house, name):
        self.happiness = 100
        self.satiety = 30
        self.name = name
        self.house = house

    def __str__(self):
        return '{} Счастье {} Сытость {}'.format(self.__class__.__name__, self.happiness, self.satiety)

    def in_depression(self):
        if self.happiness < 10:
            print('Млекопитающее', self.name, 'погибло от тоски(')
            return True

    def exhaustion(self):
        if self.satiety < 10:
            print('Млекопитающее', self.name, 'погибло от истощения(')
            return True

    def eat(self):
        if self.house.food_in_fridge > 40:
            food = randint(30, 40)
            self.satiety += food
            self.house.food_in_fridge -= food
            self.house.food += food
            return food

    def is_dirty_house(self):
        if self.house.mud > 90:
            self.happiness -= 10

    def tactile_sensations(self):
        self.happiness += 5


class House:
    fur_coat = 0
    money = 0
    food = 0

    def __init__(self):
        self.money_in_nightstand = 100
        self.food_in_fridge = 50
        self.cat_food = 30
        self.mud = 0

    def pollution(self):
        self.mud += 5

    def __str__(self):
        return '{} Деньги {} Еда {} Беспорядок {} Еда для кота {}'.format(self.__class__.__name__,
                                                                          self.money_in_nightstand, self.food_in_fridge,
                                                                          self.mud, self.cat_food)


class Husband(Mammal):

    def __str__(self):
        return super().__str__()

    def act(self):
        self.is_dirty_house()

        if self.house.food_in_fridge > 40:
            if self.satiety < 30:
                self.eat()
            elif self.happiness < 30:
                self.gaming()
            elif self.house.money_in_nightstand < 350:
                self.work()

            else:
                print('У мужа дела в ажуре!')
                dice = randint(1, 6)
                if dice == 1:
                    self.work()
                elif dice in (5, 6):
                    self.gaming()

    def eat(self):

        print('Муж поел', super().eat())

    def work(self):
        self.house.money_in_nightstand += 150
        self.satiety -= 10
        self.house.money += 150
        print('Сходил на работу')

    def gaming(self):
        self.happiness += 20
        self.satiety -= 10
        print('Расслабился в таньчики.')


class Wife(Mammal):

    def __str__(self):
        return super().__str__()

    def act(self):
        self.is_dirty_house()

        if self.satiety > 30:

            if self.house.mud > 110:
                self.clean_house()

            elif self.house.money_in_nightstand > 240:
                if self.house.food_in_fridge < 60:
                    self.shopping()
                elif self.house.cat_food < 20:
                    self.shopping()

                elif self.happiness < 70:
                    self.buy_fur_coat()
                else:
                    print('У жены дел не нашлось.')

        else:
            self.eat()
            self.tactile_sensations()

    def eat(self):

        print('Жена поела', super().eat())

    def shopping(self):
        if self.house.money_in_nightstand > 190:
            food = randint(90, 120)
            cat_food = randint(20, 30)
            self.house.food_in_fridge += food
            self.house.cat_food += cat_food
            self.satiety -= 10
            self.house.money_in_nightstand -= (food + cat_food)
            self.house.food += food
            print('Купила', food, 'еды и', cat_food, 'для котика.')

    def buy_fur_coat(self):
        if self.house.money_in_nightstand > 350:
            self.house.fur_coat += 1
            self.house.money_in_nightstand -= 350
            self.satiety -= 10
            self.happiness += 60
            print('Купила шубу.')
        else:
            print('Денег не хватает, лучше сэкономить!')
            self.satiety -= 10

    def clean_house(self):
        self.satiety -= 10
        self.house.mud -= 100
        print('Убрала дом.')

    def is_dirty_house(self):
        if home.mud > 90:
            self.happiness -= 10


class Child(Wife, Husband):

    def act(self):
        if self.satiety < 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food_in_fridge > 20:
            food = randint(7, 10)
            self.satiety += food
            self.house.food_in_fridge -= food
            self.house.food += food

    def sleep(self):
        self.satiety -= 10


class Cat(Mammal):

    def act(self):

        self.exhaustion()
        if self.satiety < 30:
            self.eat()

        dice = randint(1, 6)
        if dice == 1:
            self.soil()
        elif dice == 5:
            self.sleep()
        else:
            self.eat()

    def eat(self):
        if self.house.cat_food > 10:
            if self.satiety < 30:
                cat_food = randint(7, 10)
                self.satiety += cat_food * 2
                self.house.cat_food -= cat_food
                print('Котик поел', cat_food * 2)
        else:
            print('Еды для котика не нашлось!')

    def sleep(self):
        self.satiety -= 10
        print('Кот поспал.')

    def soil(self):
        self.satiety -= 10
        self.house.pollution()
        print('Дом стал еще грязнее! Кот ободрал обои.')


home = House()
serge = Husband(home, name='Сережа')
masha = Wife(home, name='Маша')
artem = Child(home, name='Артем')
persik = Cat(home, name='Персик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    persik.act()
    artem.act()
    home.pollution()

    if serge.in_depression():
        break
    elif masha.in_depression():
        break
    elif serge.exhaustion():
        break
    elif masha.exhaustion():
        break
    elif artem.exhaustion():
        break
    elif persik.exhaustion():
        break

    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(artem, color='cyan')
    cprint(home, color='cyan')
    cprint(persik, color='cyan')

cprint('Съедено за год {} Заработано за год {} Куплено шуб за год {}'.format(serge.house.food, serge.house.money,
                                                                             serge.house.fur_coat), color='blue')

# после реализации первой части - отдать на проверку учителю
# можете приступать ко второй части
######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачет!