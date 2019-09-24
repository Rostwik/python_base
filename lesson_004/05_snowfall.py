# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = [[(x,y), n]]

sd.resolution = (1200, 600)

N = []

for _ in range(20):
    x = sd.random_number(50, 1150)
    n = sd.random_number(10, 50)
    N.append([x, n])

print(N)
y = 600

while True:
    sd.start_drawing()
    delta = sd.random_number(2, 10)
    plus_minus = sd.random_number(0, 1)
    for i in N:

        point = sd.get_point(i[0], y)
        sd.snowflake(center=point, length=i[1], color=sd.background_color)
    y -= 5
    for i in N:
        point = sd.get_point(i[0], y)
        sd.snowflake(center=point, length=i[1], color=sd.COLOR_WHITE)
        if plus_minus:
            i[0] += delta
        else:
            i[0] -= delta

# i[0] += delta if plus_minus else i[0]-=delta TODO: в таком формате PCh подчеркивает красным выражение после else,
#                                               сигнализируя об ошибочном синтаксисе. Подскажите, пожалуйста,
#                                               почему так происходит?
    sd.finish_drawing()
    sd.sleep(0.1)


    sd.clear_screen()
    if y < 10:
        break

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


sd.pause()

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
