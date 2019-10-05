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
    n = sd.random_number(15, 40)
    snowfall.append([x, y, n])



while True:

    sd.start_drawing()

    #    цикл по номерам упавших снежинок:
    #        удаляем эту снежинку из снежинок
    #    добавляем новых снежинок сверху по количеству удаленных len(номера_упавших_снежинок)

    # Не смог реализовать алгоритм выше, так как в случае хотя бы двух элементов на удаление возникает ситуация,
    # когда после удаления первого элемента,я пытаюсь обратиться за размеры списка, либо удаляю не тот элемент
    # ведь порядок элементов "съехал" и тогда снежинка просто зависает посреди экрана. Сделал через INSERT.
    # ПОдскажите, пожалуйста, как сделать лучше, удовлетворяя предложенному алгоритму. Спасибо.

    # TODO Это важная ошибка, редактирование списка в цикле по этому же списку может привести к непредвиденным
    # TODO ситуациям.
    # TODO Можно попробовать следующую конструкцию
    # TODO for delta, index in enumerate(fallen_snowflakes):
    # TODO     snowfall.pop(index - delta)
    # TODO Это учтёт поправку смещения в номерах индексов
    # TODO Не забудьте потом добавить пару снежинок сверху, чтобы снегопад постепенно усиливался

    fallen_snowflakes = []
    for number_of_fallen_snowflakes, icecrystal in enumerate(snowfall):
        point = sd.get_point(icecrystal[0], icecrystal[1])
        sd.snowflake(center=point, length=icecrystal[2], color=sd.background_color)
        gravity = icecrystal[2] / 3
        wind = sd.random_number(1, 5)
        dir_wind = sd.random_number(0, 1)
        icecrystal[1] -= gravity
        icecrystal[0] += wind if dir_wind else -wind
        point = sd.get_point(icecrystal[0], icecrystal[1])
        sd.snowflake(center=point, length=icecrystal[2], color=sd.COLOR_WHITE)
        if icecrystal[1] < 10:
            fallen_snowflakes.append(number_of_fallen_snowflakes)
    for i in fallen_snowflakes:
        del snowfall[i]
        x = sd.random_number(50, 1150)
        y = 600
        n = sd.random_number(15, 40)
        snowfall.insert(i, [x, y, n])

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

