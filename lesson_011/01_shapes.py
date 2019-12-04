# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_any_figure(start_point_figure, length, angle):
        start_point_vector = start_point_figure
        side = int(360 / n)
        for figure_angle in range(0, 360 - side, side):
            v = sd.get_vector(start_point=start_point_vector, angle=figure_angle + angle, length=length, width=1)
            v.draw()
            start_point_vector = v.end_point
        sd.line(start_point=start_point_figure, end_point=start_point_vector)

    return draw_any_figure


draw_triangle = get_polygon(n=3)
draw_triangle(start_point_figure=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
#зачет!