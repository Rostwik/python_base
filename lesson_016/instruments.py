import datetime


def pars_date(date_str):
    date_pars = date_str.split('-')
    date_dt = datetime.date(int(date_pars[0]), int(date_pars[1]), int(date_pars[2]))
    return date_dt




# today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
# today = datetime.datetime.strptime('2020-04-01 00:00+0300', '%Y-%m-%d %H:%M%z')
# data_dt = datetime.datetime.strptime(tag.time['datetime'], '%Y-%m-%d %H:%M%z')