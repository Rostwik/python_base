# -*- coding: utf-8 -*-

# (определение функций)

import simple_draw as sd


def smile(x, y, color):
    lb_el = sd.get_point(x, y)
    rt_el = sd.get_point(x + 200, y + 170)
    sd.ellipse(left_bottom=lb_el, right_top=rt_el, color=color, width=1)
    x += 50
    y += 127
    cp = sd.get_point(x, y)
    sd.circle(center_position=cp, radius=15, color=color)
    x += 100
    cp = sd.get_point(x, y)
    sd.circle(center_position=cp, radius=15, color=color)
    l_smile = sd.get_point(x - 120, y - 60)
    mid_l_smile = sd.get_point(x - 90, y - 80)
    mid_r_smile = sd.get_point(x - 20, y - 80)
    r_smile = sd.get_point(x + 20, y - 60)
    smile_list = [l_smile, mid_l_smile, mid_r_smile, r_smile]
    sd.lines(point_list=smile_list, color=color, closed=False, width=1)


sd.resolution = (1200, 600)

for _ in range(10):
    sr_y = sd.random_number(0, 430)
    sr_x = sd.random_number(0, 1000)
    rnd_color = sd.random_color()
    smile(sr_x, sr_y, rnd_color)


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# smile(0, 430, (255, 0, 120))

sd.pause()
#зачет!