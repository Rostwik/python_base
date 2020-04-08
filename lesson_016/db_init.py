import peewee
import datetime

from playhouse.db_url import connect, DatabaseProxy

from lesson_016.instruments import pars_date


class DatabaseUpdater:

    def __init__(self, url=None):
        self.url = url
        self.table_weather = None

    def init_db(self):
        database_proxy = DatabaseProxy()

        class WeatherTable(peewee.Model):
            class Meta:
                database = database_proxy

        class Weather(WeatherTable):
            date = peewee.DateField()  # дата
            change_date = peewee.DateField() # дата изменения
            temperature = peewee.CharField()  # температура
            terms = peewee.CharField()  # погодные условия

        if self.url:
            database = connect('sqlite:///' + self.url)
        else:
            database = connect('sqlite:///default.db')

        database_proxy.initialize(database)
        database.create_tables([Weather])

        self.table_weather = Weather

    def read_db(self, number_of_days=None):

        query = self.table_weather.select().dicts()
        for row in query:
            print(row)

    def write_db(self, weather_data):

        query = self.table_weather.select().dicts()

        for day in weather_data:
            for item in query:
                day_by_str = pars_date(day)
                if item['date'] == day_by_str and item['change_date'] < datetime.date.today():
                    self.table_weather[item['id']].delete_instance()
            new_weather = self.table_weather(
                date=day,
                change_date=datetime.date.today(),
                temperature=weather_data[day][0],
                terms=weather_data[day][1])
            new_weather.save()



