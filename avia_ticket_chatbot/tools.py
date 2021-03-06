import collections
import datetime

from settings import DISPATCHER_CONFIG


def dispatcher(context):
    """
    Диспетчер выбирает все записи из файла конфигурации, где находятся все возможные маршруты.
    В маршруте может быть или определенная дата или день недели или день месяца отправлений. (последние
    два периодические) Далее маршруты сортируются и ближайшие 5 попадают в выборку для
    пользователя. Подходящими маршрутами считаются те, которые находятся в интервале 30 дней от желаемой даты.

    :param context:
    :return:
    """

    suitable_flights = collections.defaultdict(list)
    context['suitable_flights'] = {}


    for route in DISPATCHER_CONFIG:
        route_config = DISPATCHER_CONFIG[route]
        if route_config['town_from'] == context['town_from'] and route_config['town_to'] == context['town_to']:

            if route_config['day_of_week'] is not None:  # Если рейс содержит периодический маршрут по дням недели
                day_of_week(route, route_config, suitable_flights, context)
            elif route_config['day_of_month'] is not None:  # Если рейс содержит периодический маршрут по дням месяца
                day_of_month(context, route, route_config, suitable_flights)
            else:

                if context['date'] == route_config['date']:
                    flight_date = datetime.datetime.strptime(context['date'] +
                                                             ' ' + route_config['time'], '%d-%m-%Y %H:%M')
                    suitable_flights[flight_date].append(route)

    user_list_of_flights(context, suitable_flights)


def user_list_of_flights(context, suitable_flights):
    list_of_suitable_flights = list(suitable_flights.keys())
    list_of_suitable_flights.sort()
    list_of_suitable_flights = list_of_suitable_flights[:5]

    for index, flight in enumerate(list_of_suitable_flights):
        context['suitable_flights'][str(index)] = [
            suitable_flights[list_of_suitable_flights[index]],
            list_of_suitable_flights[index].strftime('%d-%m-%Y %H:%M')]

    context['suitable_flights_user_text'] = ' ,'.join(
        f"<br> {x}. Рейс: {', '.join(context['suitable_flights'][x][0])}, "
        f" Дата и время вылета: {context['suitable_flights'][x][1]}"
        for x in context['suitable_flights'] if not None)

    # print(context['suitable_flights_user_text'])


def day_of_month(context, route, route_config, suitable_flights):
    user_date = datetime.datetime.strptime(context['date'], '%d-%m-%Y')
    month_period = user_date + datetime.timedelta(days=30)
    for day_of_the_month in route_config['day_of_month'].split(','):
        user_date_0 = user_date
        while user_date_0 < month_period:
            if user_date_0.day == int(day_of_the_month):
                flight_date = datetime.datetime.strptime(user_date_0.strftime('%d-%m-%Y') +
                                                         ' ' + route_config['time'], '%d-%m-%Y %H:%M')
                suitable_flights[flight_date].append(route)

            user_date_0 = user_date_0 + datetime.timedelta(days=1)


def day_of_week(route, route_config, suitable_flights, context):
    user_date = datetime.datetime.strptime(context['date'], '%d-%m-%Y')
    month_period = user_date + datetime.timedelta(days=30)
    for weekday in route_config['day_of_week'].split(','):
        user_date_0 = user_date
        while user_date_0 < month_period:
            if user_date_0.weekday() == int(weekday):
                flight_date = datetime.datetime.strptime(user_date_0.strftime('%d-%m-%Y') +
                                                         ' ' + route_config['time'], '%d-%m-%Y %H:%M')
                suitable_flights[flight_date].append(route)

            user_date_0 = user_date_0 + datetime.timedelta(days=1)
