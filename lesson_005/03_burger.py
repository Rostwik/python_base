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

from lesson_005.my_burger import cutlet, bun, mustard_sauce, onion, gherkin, cheese, Seasoning_grill, sausages, \
    tomato, mayonnaise

# TODO Нэйминг! Никакого верхнего регистра, все буквы одного, небольшого, размера.
# TODO + стоит добавить глагол - сделать_двойной_чизбургер например)
def Double_Cheeseburger():
    print('Представляем Вашему вниманию секретный рецепт Двойного чизбургера!')
    cutlet()
    bun()
    mustard_sauce()
    onion()
    gherkin()
    cheese()
    Seasoning_grill()


def Megaburger():  # TODO И тут
    print('Представляем Вашему вниманию секретный рецепт Баварского бургера!')
    sausages()
    bun()
    onion()
    gherkin()
    tomato()
    cheese()
    mayonnaise()


Double_Cheeseburger()
Megaburger()