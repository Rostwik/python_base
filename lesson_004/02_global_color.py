# -*- coding: utf-8 -*-

import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_any_figure(start_point_figure, length, angle, color_figure, figure=3):
    start_point_vector = start_point_figure
    side = int(360 / figure)
    for i in range(0, 360 - side, side):  # TODO Нэйминг, меняем i на angle
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


colors = {'0': {'name': 'red', 'in_sd': sd.COLOR_RED},
          '1': {'name': 'orange', 'in_sd': sd.COLOR_ORANGE},
          '2': {'name': 'yellow', 'in_sd': sd.COLOR_YELLOW},
          '3': {'name': 'green', 'in_sd': sd.COLOR_GREEN},
          '4': {'name': 'cyan', 'in_sd': sd.COLOR_CYAN},
          '5': {'name': 'blue', 'in_sd': sd.COLOR_BLUE},
          '6': {'name': 'purple', 'in_sd': sd.COLOR_PURPLE}
          }

for i in range(7):  # TODO используйте метод .items() и цикл по словарю, как в lesson 3 - 05
    print(i, ': ', colors[str(i)]['name'])

user_color = input('Введите желаемый цвет: ')
# TODO С помощью бесконечного цикла проверьте правильность ввода пользователем
# TODO Затем, вне цикла, рисуйте фигуры с полученным и проверенным выбором пользователя
if user_color in colors.keys():
    point = sd.get_point(100, 100)
    length = 80
    figures_color = colors[str(user_color)]['in_sd']
    triangle(point=point, length=length, angle=20, color_figure=figures_color)
    point = sd.get_point(400, 100)
    length = 80
    figures_color = colors[str(user_color)]['in_sd']
    square(point=point, length=length, angle=20, color_figure=figures_color)
    point = sd.get_point(100, 350)
    length = 80
    figures_color = colors[str(user_color)]['in_sd']
    pentagon(point=point, length=length, angle=20, color_figure=figures_color)
    point = sd.get_point(400, 350)
    length = 80
    figures_color = colors[str(user_color)]['in_sd']
    hexagon(point=point, length=length, angle=20, color_figure=figures_color)
else:
    print('Вы ввели некорректный номер!')

sd.pause()
