import math
import random
from django.db.models import Max
from googletrans import Translator


def get_max_id(model):
    return list(model.objects.aggregate(Max('id')).values())[0]


def get_random_record(model, max_id=None):
    if max_id is None:
        max_id = get_max_id(model)
    random_id = math.ceil(max_id * random.random())
    return model.objects.filter(id__gte=random_id)[0]


def format_field(field):
    MISSING_VAL = 'Anonymous' # 'N/A'
    if field is not None:
        field = str(field).strip()
    return field or MISSING_VAL


def translate(text):
    translator = Translator()
    translated = translator.translate(text)

    return (translated.text, translated.src)
