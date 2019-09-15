# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (600, 600)
delta = 0
# TODO хорошая работа! Но стиль можно красиво упростить
# TODO вместо ручного счёта рядов - добавьте enumerate() к первому циклу
# TODO что-то вроде: фор дельта, игрик ин энумерэйт(рэндж(..)):
for y in range(0, 700, 50):
    delta += 1
    flag = delta % 2
    for x in range(0, 700, 100):
        # TODO вместо флаг можно просто вставлять условие delta % 2 - будет понятно и просто
        # TODO внутри практически одинаковые записи, меняются только переменные
        # TODO можно использовать короткую запись условия для изменения одной лишь переменной
        # TODO х0 равен х - 50 если дельта % 2 в ином случае х
        # TODO а дальше брать точки используя х0
        if flag:
            l_point = sd.get_point(x - 50, y)
            t_point = sd.get_point(x + 50, y + 50)
        else:
            l_point = sd.get_point(x, y)
            t_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(left_bottom=l_point, right_top=t_point, width=2)

sd.pause()
