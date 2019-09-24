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

def draw_any_figure(start_point_figure, length, color_figure, figure=3):
    angle_figure = 360 / figure
    start_point_vector = start_point_figure
    for i in range(figure - 1):
        angle = i * angle_figure
        v = sd.get_vector(start_point=start_point_vector, angle=angle, length=length, width=1)
        v.draw(color=color_figure)
        start_point_vector = v.end_point
    sd.line(start_point=start_point_figure, end_point=start_point_vector, color=color_figure)


figures_color = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                 sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

print('Возможные цвета', '\n', '0 : red', '\n', '1 : orange', '\n', '2 : yellow', '\n', '3 : green',
      '\n', '4 : cyan', '\n', '5 : blue', '\n', '6 : purple')

user_color = int(input('Введите желаемый цвет: '))

if user_color in range(7):
    point = sd.get_point(100, 100)
    length = 80
    draw_any_figure(start_point_figure=point, length=length, color_figure=figures_color[user_color], figure=3)

    point = sd.get_point(400, 100)
    length = 80
    draw_any_figure(start_point_figure=point, length=length, color_figure=figures_color[user_color], figure=4)

    point = sd.get_point(100, 350)
    length = 80
    draw_any_figure(start_point_figure=point, length=length, color_figure=figures_color[user_color], figure=5)

    point = sd.get_point(400, 350)
    length = 80
    draw_any_figure(start_point_figure=point, length=length, color_figure=figures_color[user_color], figure=6)
else:
    print('Вы ввели некорректный номер!')

sd.pause()
