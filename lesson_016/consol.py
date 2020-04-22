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

menu = {'1': {'name': 'Добавить прогнозы за диапазон дат в базу данных', 'func': perfect_day.weather_html},
        '2': {'name': 'Получить прогнозы за диапазон дат из базы', 'func': test.read_db},
        '3': {'name': 'Создать открытку за дату', 'func': card.draw_a_card},
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

    if i == '1':

        l_data, r_data = input_date_range()
        weather_data = perfect_day.weather_html(l_data, r_data, False)
        pprint(weather_data)
        test.write_db(weather_data)

    elif i == '2':
        l_data, r_data = input_date_range()
        menu['2']['func'](l_data, r_data)
        
    elif i == '3':
        while True:
            date_postcard = input('Введите дату в формате (yyyy-mm-dd): ')
            if format_date(date_postcard):
                break

        read_postcard_data = menu['2']['func'](date_postcard, date_postcard)
        if read_postcard_data:
            menu['3']['func'](read_postcard_data[0][1], read_postcard_data[0][2], date_postcard)

    elif i == '4':
        menu['4']['func']()
        break

    choice = False
