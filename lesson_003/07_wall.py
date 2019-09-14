# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (600, 600)
delta = 0

for y in range(0, 700, 50):
    delta += 1
    flag = delta % 2
    for x in range(0, 700, 100):
        if flag:
            l_point = sd.get_point(x - 50, y)
            t_point = sd.get_point(x + 50, y + 50)
        else:
            l_point = sd.get_point(x, y)
            t_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(left_bottom=l_point, right_top=t_point, width=2)

sd.pause()
