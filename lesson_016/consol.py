from pprint import pprint

from lesson_016.db_init import DatabaseUpdater
from lesson_016.db_weather import WeatherMaker, ImageMaker
from lesson_016.instruments import format_date, exit_bb, input_date_range

perfect_day = WeatherMaker('https://yandex.ru/pogoda/saint-petersburg')
weather_data = perfect_day.weather_html()
pprint(weather_data)

test = DatabaseUpdater()
test.init_db()
test.write_db(weather_data)

card = ImageMaker()


def add_date_range():
    l_data, r_data = input_date_range()
    weather_data = perfect_day.weather_html(l_data, r_data, False)
    pprint(weather_data)
    test.write_db(weather_data)
    print('Данные записаны в бд.')


def get_forecasts():
    l_data, r_data = input_date_range()
    test.read_db(l_data, r_data)
    print('Данные получены из бд.')

def create_postcard():
    while True:

        date_postcard = input('Введите дату в формате (yyyy-mm-dd): ')
        if format_date(date_postcard):
            break

    read_postcard_data = test.read_db(date_postcard, date_postcard)
    if read_postcard_data:
        card.draw_a_card(read_postcard_data[0][1], read_postcard_data[0][2], date_postcard)

    print('Открытка создана.')


menu = {'1': {'name': 'Добавить прогнозы за диапазон дат в базу данных', 'func': add_date_range},
        '2': {'name': 'Получить прогнозы за диапазон дат из базы', 'func': get_forecasts},
        '3': {'name': 'Создать открытку за дату', 'func': create_postcard},
        '4': {'name': 'Выход', 'func': exit_bb}
        }

print('Добро пожаловать в WeatherMaker! Выберите один из пунктов ниже:')
choice = False

while True:
    for i, func in menu.items():
        print(i, ': ', func['name'])

    while not choice:
        i = input('Ваш выбор:')
        if i not in menu or not i.isdigit() or len(i) != 1:
            print('Вы ввели некорректный символ! Попробуйте еще раз.')
        else:
            choice = True

    menu[i]['func']()

    if i == '4':
        break

    choice = False

