# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger

#TODO почему-то не подкидывает после точки доступные функции модуля my_burger. Нужно как-то поднастроить PCh?

def Double_Cheeseburger():
    print('Представляем Вашему вниманию секретный рецепт Двойного чизбургера!')
    my_burger.cutlet()
    my_burger.bun()
    my_burger.mustard_sauce()
    my_burger.onion()
    my_burger.gherkin()
    my_burger.cheese()
    my_burger.Seasoning_grill()

def Megaburger():
    print('Представляем Вашему вниманию секретный рецепт Баварского бургера!')
    my_burger.sausages()
    my_burger.bun()
    my_burger.onion()
    my_burger.gherkin()
    my_burger.tomato()
    my_burger.cheese()
    my_burger.mayonnaise()


Double_Cheeseburger()
Megaburger()