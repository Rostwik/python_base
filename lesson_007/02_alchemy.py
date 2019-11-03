# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


#  Кстати для сравнения будет корректнее использовать isinstance(object_1, object_2)"
#  Я не разобрался с Вашей подсказкой, в этой домашней работе мы еще не добрались до наследования.
#  Подскажите, пож., как мне применить  isinstance. Саму функцию изучил.


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Earth):
            return Dirt()
        if isinstance(other, Fire):
            return Steam()

    def __str__(self):
        return self.__class__.__name__


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()

    def __str__(self):
        return self.__class__.__name__


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Water):
            return Water()
        if isinstance(other, Earth):
            return Lava()

    def __str__(self):
        return self.__class__.__name__


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()

    def __str__(self):
        return self.__class__.__name__


class Storm:
    def __str__(self):
        return self.__class__.__name__


class Steam:

    def __str__(self):
        return self.__class__.__name__


class Dirt:

    def __str__(self):
        return self.__class__.__name__


class Lightning:

    def __str__(self):
        return self.__class__.__name__


class Dust:

    def __str__(self):
        return self.__class__.__name__


class Lava:

    def __str__(self):
        return self.__class__.__name__


print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Fire(), '=', Fire() + Fire())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Fire(), '+', Earth(), '=', Earth() + Fire())
print(Water(), '+', Fire(), '=', Water() + Fire())

# Water, Air, Fire, Earth, Storm, Steam, Dirt, Lightning, Dust, Lava

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
