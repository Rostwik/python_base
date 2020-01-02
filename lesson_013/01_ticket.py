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
#  Фраза означает, что нужна перезагрузка, однако у вас там что-то очень много завизимостей прописано
#  И файл должен быть расположен внутри 13-ого урока, а не снаружи
# TODO: как я усвоил, возможно ошибочно, файл создается на проект(окружение), поэтому он снаружи.
#  он создался после выполнения стандартных команд. Потом я удалил этот файл и попробовал создать вновь,
#  ничего не вышло. Я не устанавливал дополнительные библиотеки, кроме тех, что в лекциях. Какие будут
#  рекомендации? Как правильно поступить?
def make_ticket(fio, from_, to, date):
    im = Image.open("images/ticket_template.png")
    print(im.format, im.size, im.mode)


    im = Image.open("images/ticket_template.png")
    font = ImageFont.truetype('ofont.ru_Baskerville_WGL4_BT.ttf', size=22)
    # не срабатывают  atl+shift+enter (
    #  Не понял, что не срабатывает?
    # TODO: это быстрая комбинация для добавления импорта, у меня не работает. Например я забыл
    #  добавить импорт потом написал random он подчеркнулся красным, не всегда работают
    #  горячие клавиши, с чем это может быть связано?
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
