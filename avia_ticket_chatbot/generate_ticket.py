from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

TAMPLATE_PATH = 'files/ticket_template.png'
FONT_PATH = 'files/Roboto-Regular.ttf'
FONT_SIZE = 25

BLACK = (0, 0, 0, 255)
NAME_OFFSET = (45, 115)
TO_OFFSET = (45, 250)
FROM_OFFSET = (45, 182)
ROUTE_OFFSET = (45, 320)
DATE_OFFSET = (255, 254)
TIME_OFFSET = (430, 254)


def generate_ticket(context):
    base = Image.open(TAMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    route = context['route'][0][0]
    date, time = context['route'][1].split(' ')

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, context['name'], font=font, fill=BLACK)
    draw.text(FROM_OFFSET, context['town_from'], font=font, fill=BLACK)
    draw.text(TO_OFFSET, context['town_to'], font=font, fill=BLACK)
    draw.text(ROUTE_OFFSET, route, font=font, fill=BLACK)
    draw.text(DATE_OFFSET, date, font=font, fill=BLACK)
    draw.text(TIME_OFFSET, time, font=font, fill=BLACK)

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    # base.save('files/ticket-example.png', 'png')
    temp_file.seek(0)

    return temp_file


