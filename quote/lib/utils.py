import math
import random
from django.db.models import Max
from googletrans import Translator


def get_max_id(model):
    """ 
    Get Max ID from Django data model
    
    Parameters: 
    model (django.db.models.Model): model
  
    Returns: 
    int: record Id 
  
    """
    return list(model.objects.aggregate(Max('id')).values())[0]


def get_random_record(model, max_id=None):
    """ 
    Get quasi-random record from Django data model
    
    Parameters: 
    model (django.db.models.Model): model
    max_id (int): max value of ID in model

    Returns: 
    QuerySet
  
    """
    if max_id is None:
        max_id = get_max_id(model)
    random_id = math.ceil(max_id * random.random())
    return model.objects.filter(id__gte=random_id).first()


def format_field(field):
    """ 
    Format field to display meaningful text instead None
    
    Parameters: 
    field (object)

    Returns: 
    string: formatted field
  
    """
    MISSING_VAL = 'Anonymous' # 'N/A'
    if field is not None:
        field = str(field).strip()
    return field or MISSING_VAL


def translate(text):
    """ 
    Traslate text
    
    Parameters: 
    text (string): text to be translated to English

    Returns: 
    tuple: (translated text, detected language of the source)
  
    """
    translator = Translator()
    translated = translator.translate(text)

    return (translated.text, translated.src)
