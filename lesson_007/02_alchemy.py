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


# TODO Интересный способ :)
# TODO Однако странная выходит ситуация, когда несколько классов обращаются к внешней функции
# TODO Надо добавить подобную функцию каждому классу отдельно.
# TODO Кстати для сравнения будет корректнее использовать isinstance(object_1, object_2)
# TODO И стоит учесть вариант, когда не подходит ни один элементов (вернуть None)
def magic(*args):
    if sorted(args) == ['Air', 'Water']:
        return Storm()
    if sorted(args) == ['Air', 'Fire']:
        return Lightning()
    if sorted(args) == ['Earth', 'Water']:
        return Dirt()
    if sorted(args) == ['Air', 'Earth']:
        return Dust()
    if sorted(args) == ['Earth', 'Fire']:
        return Lava()
    if sorted(args) == ['Fire', 'Water']:
        return Steam()


class Water:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Air:
    def __add__(self, other):
        probe = (self.__class__.__name__, other.__class__.__name__)

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Fire:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Earth:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Storm:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Steam:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Dirt:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Lightning:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Dust:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


class Lava:
    def __add__(self, other):
        probe = [self.__class__.__name__, other.__class__.__name__]

        return magic(*probe)

    def __str__(self):
        return self.__class__.__name__


print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Fire(), '=', Fire() + Fire())
print(Fire(), '+', Earth(), '=', Fire() + Earth())

# Water, Air, Fire, Earth, Storm, Steam, Dirt, Lightning, Dust, Lava

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
