from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEvent

from vkbot import BotVk

from chatbot import settings
from chatbot.generate_ticket import generate_ticket


def isolated_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper


class Test1(TestCase):
    RAW_EVENT = {'type':
                     'message_new',
                 'object':
                     {
                         'message':
                             {'date': 1580758563, 'from_id': 840163, 'id': 108, 'out': 0, 'peer_id': 840163,
                              'text': 'чотам', 'conversation_message_id': 105, 'fwd_messages': [], 'important': False,
                              'random_id': 0, 'attachments': [], 'is_hidden': False},
                         'client_info':
                             {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                              'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}
                     },
                 'group_id': 190258846,
                 'event_id': '67e64c880f573d353203cdb10677b53399da7d80'
                 }

    INPUTS = [
        'Привет',
        'А когда?',
        'Где будет конференция?',
        'Зарегистрируй меня',
        'Вениамин',
        'мой адрес email@email.ru',
    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],

        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Вениамин', email='email@email.ru')
    ]

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count  # [obj, obj, ...]
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('vkbot.vk_api.VkApi'):
            with patch('vkbot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = BotVk('', '')
                bot.on_event = Mock()
                bot.send_image = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == 5

    # def test_on_event(self):
    # старый тест
    #     event = VkBotMessageEvent(raw=self.RAW_EVENT)
    #
    #     send_mock = Mock()
    #
    #     with patch('vkbot.vk_api.VkApi'):
    #         with patch('vkbot.VkBotLongPoll'):
    #             bot = BotVk('', '')
    #             bot.api = Mock()
    #             bot.api.messages.send = send_mock
    #
    #             bot.on_event(event)
    #
    #     send_mock.assert_called_once_with(
    #         message=self.RAW_EVENT['object']['message']['text'],
    #         random_id=ANY,
    #         peer_id=self.RAW_EVENT['object']['message']['peer_id']
    #     )

    #       Я не понял, зачем лектор вставил ANY если по формату требуется случайное число?
    #       Чем это вредит тестам?
    #       Не понял как работает ANY в данном примере. random_id теперь это объект ANY, у которого
    #       ничего нет кроме переопределенных методов для сравнения. Но у нас в данном случае нет никаких
    #       сравнений. Можете поделиться ссылкой на разъяснения и примеры по поводу ANY ?

    @isolated_db
    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('vkbot.VkBotLongPoll', return_value=long_poller_mock):
            bot = BotVk('', '')
            bot.api = api_mock
            bot.send_image = Mock()
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])

        assert real_outputs == self.EXPECTED_OUTPUTS

    def test_image_generation(self):
        with open('files/email.png', 'rb') as avatar_file:
            avatar_mock = Mock()
            avatar_mock.content = avatar_file.read()

        with patch('requests.get', return_value=avatar_mock):
            ticket_file = generate_ticket('name', 'email')

        with open('files/ticket-example.png', 'rb') as expected_file:
            expected_bytes = expected_file.read()

        assert ticket_file.read() == expected_bytes
