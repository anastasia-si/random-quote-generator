import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from quote.models import Author, Quote, QuoteType
from quote.forms import AddQuoteForm

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


def add_quote(request):
    
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddQuoteForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home')) # redirect back to the home page

    else:
        form = AddQuoteForm()

    context = {
        'form': form
    }

    return render(request, 'quote/add_quote.html', context)