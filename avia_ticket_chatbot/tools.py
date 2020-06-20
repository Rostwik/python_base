import collections
import datetime

from avia_ticket_chatbot.settings import DISPATCHER_CONFIG


def dispatcher(context):
    """
    Диспетчер выбирает все записи из файла конфигурации, где находятся все возможные маршруты.
    В маршруте может быть или определенная дата или день недели или день месяца отправлений. (последние
    два периодические) Далее маршруты сортируются и ближайшие 5 попадают в выборку для
    пользователя. Если маршрут периодический, то сравнение производится с текущей датой, удовлетворяющим
    условиям считается маршрут в рамках 30 календарных дней от даты запроса.

    :param context:
    :return:
    """

    suitable_flights = collections.defaultdict(list)
    context['suitable_flights'] = {}

    for route in DISPATCHER_CONFIG:
        route_config = DISPATCHER_CONFIG[route]
        if route_config['town_from'] == context['town_from'] and route_config['town_to'] == context['town_to']:

            if route_config['day_of_week'] is not None:
                day_of_week(route, route_config, suitable_flights, context)

    list_of_suitable_flights = list(suitable_flights.keys())
    list_of_suitable_flights.sort()
    for index in range(5):
        context['suitable_flights'][index] = [suitable_flights[list_of_suitable_flights[index]],
                                              list_of_suitable_flights[index]]

    context['suitable_flights_user_text'] = ' ,'.join(
        f"<br> {x}. Рейс: {context['suitable_flights'][x][0]}"
        f" Дата и время вылета: {context['suitable_flights'][x][1].strftime('%d-%m-%Y %H:%M')}"
        for x in context['suitable_flights'])


def day_of_week(route, route_config, suitable_flights, context):
    for weekday in route_config['day_of_week'].split(','):
        user_date = datetime.datetime.strptime(context['date'], '%d-%m-%Y')

        month_period = user_date + datetime.timedelta(days=30)
        while user_date < month_period:
            if user_date.weekday() == int(weekday):
                flight_date = datetime.datetime.strptime(user_date.strftime('%d-%m-%Y') +
                                                         ' ' + route_config['time'], '%d-%m-%Y %H:%M')
                suitable_flights[flight_date].append(route)

            user_date = user_date + datetime.timedelta(days=1)
