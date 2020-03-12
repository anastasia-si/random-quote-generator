from django.shortcuts import render
from django.views import generic
from quote.models import Author, Quote, QuoteType
from .lib import utils as utils
from .lib import quotation as q
from .lib import quote_formatter as qf


def home(request):
    """View function for home page of site."""
    
    random_quote = utils.get_random_record(Quote)
    quote_txt = random_quote.text
    quote_formatter = qf.QuoteFormatter()
    formatted_txt = quote_formatter.beautify(q.AdvancedQuotation(quote_txt))

    date = random_quote.created_date

    user = utils.format_field(random_quote.user)

    author = utils.format_field(random_quote.author)

    tag_list = [quote_type.get_name_display() for quote_type in random_quote.quotetype.all()]
    tags = ', '.join(tag_list)

    context = {
        'text': formatted_txt,
        'author': author,
        'user': user,
        'tags': tags,
        'date': date
    }

    return render(request, 'home.html', context=context)
