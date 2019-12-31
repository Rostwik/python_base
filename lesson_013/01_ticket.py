# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageFont, ImageDraw, ImageColor


# Note: you may need to restart the kernel to use updated packages.  Подскажите, пожалуйста, что
# означает эта фраза? У меня оущещние, что файл requirements.txt  не обновляется.
# TODO Фраза означает, что нужна перезагрузка, однако у вас там что-то очень много завизимостей прописано
# TODO И файл должен быть расположен внутри 13-ого урока, а не снаружи
def make_ticket(fio, from_, to, date):
    im = Image.open("images/ticket_template.png")
    print(im.format, im.size, im.mode)

    im = Image.open("images/ticket_template.png")
    font = ImageFont.truetype('ofont.ru_Baskerville_WGL4_BT.ttf', size=22)
    # не срабатывают  atl+shift+enter (
    # TODO Не понял, что не срабатывает?
    im_txt = ImageDraw.Draw(im)
    im_txt.text((45, 130), fio, font=font, fill=ImageColor.colormap['black'])
    im_txt.text((45, 195), from_, font=font, fill=ImageColor.colormap['black'])
    im_txt.text((45, 265), to, font=font, fill=ImageColor.colormap['black'])
    im_txt.text((250, 265), date, font=font, fill=ImageColor.colormap['black'])
    im.show()  # TODO Картинку лучше сохранять, через save()


passenger = 'Иванов П.А.'
departure = 'Москва'
arrival = 'Санкт-Петербург'
data = '24.12.2020'

make_ticket(passenger, departure, arrival, data)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
