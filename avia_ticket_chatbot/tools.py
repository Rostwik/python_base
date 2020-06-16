from avia_ticket_chatbot.settings import DISPATCHER_CONFIG


def dispatcher(context):
    suitable_flights = []
    for number, route in enumerate(DISPATCHER_CONFIG):
        if DISPATCHER_CONFIG[route]['town_from'] == context['town_from'] and DISPATCHER_CONFIG[route]['town_to'] == context['town_to']:
            suitable_flights.append(route)
            context['suitable_flights'] = ' ,'.join(suitable_flights)
