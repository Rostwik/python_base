# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_any_figure(start_point_figure, length, angle, color_figure, figure=3):
    start_point_vector = start_point_figure
    side = int(360 / figure)
    for i in range(0, 360 - side, side):
        v = sd.get_vector(start_point=start_point_vector, angle=i + angle, length=length, width=1)
        v.draw(color=color_figure)
        start_point_vector = v.end_point
    sd.line(start_point=start_point_figure, end_point=start_point_vector, color=color_figure)


def triangle(point, length, angle, color_figure):
    draw_any_figure(start_point_figure=point, length=length, angle=angle, color_figure=color_figure, figure=3)


def square(point, length, angle, color_figure):
    draw_any_figure(start_point_figure=point, length=length, angle=angle, color_figure=color_figure, figure=4)


def pentagon(point, length, angle, color_figure):
    draw_any_figure(start_point_figure=point, length=length, angle=angle, color_figure=color_figure, figure=5)


def hexagon(point, length, angle, color_figure):
    draw_any_figure(start_point_figure=point, length=length, angle=angle, color_figure=color_figure, figure=6)


figures = {'0': {'name': 'Треугольник', 'func': triangle},
           '1': {'name': 'Квадрат', 'func': square},
           '2': {'name': 'Пятиугольник', 'func': pentagon},
           '3': {'name': 'Шестиугольник', 'func': hexagon}
           }

for i, j in figures.items():
    print('Возможные фигуры:', i, ': ', j['name'])

user_figure = input('Введите желаемую фигуру: ')

while user_figure not in figures.keys():
    print('Вы ввели некорректный номер фигуры!')
    user_figure = input('Введите желаемую фигуру: ')

point = sd.get_point(300, 300)
length = 80
func_of_dict = figures[user_figure]['func']
func_of_dict(point=point, length=length, angle=0, color_figure=sd.COLOR_GREEN)


sd.pause()
