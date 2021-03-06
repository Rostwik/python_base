# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(100, 100)

for i in range(0, 15, 5):
    sd.circle(center_position=point, radius=50 + i, color=(125, 0, 250), width=1)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

def circle_ex(point_cir, step, color_ex):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point_cir, radius=radius, color=color_ex)


point = sd.get_point(400, 200)
circle_ex(point_cir=point, step=10, color_ex=sd.random_color())

# Нарисовать 10 пузырьков в ряд

for x in range(200, 1200, 100):
    point = sd.get_point(x, 550)
    circle_ex(point_cir=point, step=5, color_ex=sd.random_color())

# Нарисовать три ряда по 10 пузырьков


for x in range(200, 1200, 100):
    for y in range(200, 500, 100):
        point = sd.get_point(x, y)
        circle_ex(point_cir=point, step=8, color_ex=sd.random_color())

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    circle_ex(point_cir=point, step=5, color_ex=color)


sd.pause()
#зачет!