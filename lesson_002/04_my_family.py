#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Отец', 'Мать', 'Дочь']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Василий', 159],
    ['Татьяна', 155],
    ['Елена', 157]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Рост отца -', my_family_height[0][1], 'см')
# TODO когда вычислений становится больше пары, их лучше вынести из принта в отдельную переменную
print('Общий рост моей семьи -', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1], 'см')
