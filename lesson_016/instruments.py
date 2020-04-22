import datetime
import time


def pars_date(date_str):
    """
    Форматируем строку в дату.
    :param date_str:
    :return:
    """
    date_pars = date_str.split('-')
    date_dt = datetime.date(int(date_pars[0]), int(date_pars[1]), int(date_pars[2]))
    return date_dt


def format_date(date):
    """
    Проверяем корректность ввода пользователя.
    :param date:
    :return:
    """

    try:
        valid_date = time.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Неверный формат, попробуйте еще!')
        return False
    return True


def input_date_range():
    while True:
        while True:
            date_left = input('Введите левый диапазон в формате (yyyy-mm-dd): ')
            if format_date(date_left):
                break
        while True:
            date_right = input('Введите правый диапазон в формате (yyyy-mm-dd): ')
            if format_date(date_right):
                break

        valid_date_right = time.strptime(date_right, '%Y-%m-%d')
        valid_date_left = time.strptime(date_left, '%Y-%m-%d')
        if valid_date_right <= valid_date_left:
            print('Левый диапазон больше правого.')
        else:
            break

    return date_left, date_right


def exit_bb():
    print('Всего доброго!')

# today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
# today = datetime.datetime.strptime('2020-04-01 00:00+0300', '%Y-%m-%d %H:%M%z')
# data_dt = datetime.datetime.strptime(tag.time['datetime'], '%Y-%m-%d %H:%M%z')
