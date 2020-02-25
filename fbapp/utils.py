import random

from .models import Gender, Content


def find_content(gender: str) -> Content:
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)
