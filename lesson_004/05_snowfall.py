# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

sd.resolution = (1200, 600)

snowfall = []

for _ in range(20):
    x = sd.random_number(50, 1150)
    y = 600
    n = sd.random_number(8, 40)
    snowfall.append([x, y, n])

# i[0] += delta if plus_minus else i[0]-=delta
# TODO: в таком формате PCh подчеркивает красным выражение после else,
# TODO: сигнализируя об ошибочном синтаксисе. Подскажите, пожалуйста,
# TODO: почему так происходит?

while True:

    sd.start_drawing()

    for i in snowfall:
        point = sd.get_point(i[0], i[1])
        sd.snowflake(center=point, length=i[2], color=sd.background_color)

    for i in snowfall:
        gravity = i[2] / 3
        wind = sd.random_number(10, 50)
        dir_wind = sd.random_number(0, 1)
        i[1] -= gravity
        if dir_wind:
            i[0] += wind
        else:
            i[0] -= wind

    for i in snowfall:
        point = sd.get_point(i[0], i[1])
        sd.snowflake(center=point, length=i[2], color=sd.COLOR_WHITE)
        if i[1] < 10:
            i[1] = 600

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# y = 500
# x = 100
#
# y2 = 450
# x2 = 150
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 50:
#         break
#     x = x + 10
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 10
#     if y2 < 50:
#         break
#     x2 = x2 + 20
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
