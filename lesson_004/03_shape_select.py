# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_any_figure(start_point_figure, length, color_figure, figure=3):
    angle_figure = 360 / (figure + 3)
    start_point_vector = start_point_figure
    for i in range(figure + 2):
        angle = i * angle_figure
        v = sd.get_vector(start_point=start_point_vector, angle=angle, length=length, width=1)
        v.draw(color=color_figure)
        start_point_vector = v.end_point
    sd.line(start_point=start_point_figure, end_point=start_point_vector, color=color_figure)


# TODO здесь нужна будет структура данных идентичная той, которую я описал в 02
# TODO словарь со словарями. Чтобы хранить в словаре функцию, не выполняя её при создании словаря,
# TODO надо написать название функции без (параметры)
# TODO функции_для_фигур = {'0': {'name': 'red', 'func': triangle},...}
# TODO Запуск такой функции тоже не совсем обычен:
# TODO функция_рисования = функции_для_фигур['0']['func']
# TODO функция_рисования(параметры)
print('Возможные фигуры: ', '\n', '0 : треугольник', '\n', '1 : квадрат', '\n', '2 : пятиугольник', '\n',
      '3 : шестиугольник')

user_figure = int(input('Введите желаемую фигуру: '))

if user_figure in range(4):
    point = sd.get_point(300, 300)
    length = 80
    draw_any_figure(start_point_figure=point, length=length, color_figure=sd.COLOR_ORANGE, figure=user_figure)
else:
    print('Вы ввели некорректный номер фигуры!')

sd.pause()
