# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (600, 600)

for delta, y in enumerate(range(0, 700, 50)):
    for x in range(0, 700, 100):
        if delta % 2:  # TODO в таких ситуация можно использовать крутое сокращение
            # TODO x0 = x - 50 if delta % 2 else x - одна изящная строка заменит 4 :) настоящий пайтон-стайл
            # TODO не то, чтобы это ошибка - просто захотелось показать такую фишку, пока есть другие правки)
            x0 = x - 50
        else:
            x0 = x
        l_point = sd.get_point(x0, y)
        t_point = sd.get_point(x0 + 100, y + 50)
        sd.rectangle(left_bottom=l_point, right_top=t_point, width=2)

sd.pause()
