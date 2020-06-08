from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TAMPLATE_PATH = 'files/ticket-base.png'
FONT_PATH = 'files/Roboto-Regular.ttf'
FONT_SIZE = 30

BLACK = (0, 0, 0, 255)
NAME_OFFSET = (255, 207)
EMAIL_OFFSET = (255, 240)

AVATAR_SIZE = 100
AVATAR_OFFSET = 100, 200


def generate_ticket(name, email):
    base = Image.open(TAMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK)

    response = requests.get(url=f'https://api.adorable.io/avatars/{AVATAR_SIZE}/{email}')
    avatar_file_like = BytesIO(response.content)
    avatar = Image.open(avatar_file_like)

    base.paste(avatar, AVATAR_OFFSET)

    # with open('files/ticket-example.png', 'wb') as f:
    #     base.save(f, 'png')

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file


# generate_ticket('name', 'email')