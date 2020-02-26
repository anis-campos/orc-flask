import os
import random
import textwrap

from PIL import Image, ImageFont, ImageDraw

from .config import basedir


def _base() -> Image:
    img = Image.new('RGB', (1200, 630), '#18BC9C')
    return img


def print_on_img(img: Image, text: str, front_size: int, height: int):
    font = ImageFont.truetype(os.path.join(basedir, 'static', 'fonts', "Arcon-Regular.otf"), front_size)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font)
    position = ((img.width - w) / 2, height)
    draw.text(position, text, (255, 255, 255), font=font)
    return w, h


def _path(uid):
    return os.path.join(basedir, 'static', 'tmp', '{}.jpg'.format(uid))


def _location(uid):
    return 'tmp/{}.jpg'.format(uid)


class OpenGraphImage:

    def __init__(self, uid, first_name: str, description):
        background: Image = _base()
        print_on_img(background, first_name.capitalize(), 70, 50)
        sentences = textwrap.wrap(description, width=60)
        current_h, pad = 180, 10
        for sentence in sentences:
            w, h = print_on_img(background, sentence, 40, current_h)
            current_h += h + pad
        self.image = background
        background.save(_path(uid))
        self.location = _location(uid)


def find_content(gender: str):
    """

    :param gender:
    :return: Content
    """
    from .models import Gender, Content
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)
