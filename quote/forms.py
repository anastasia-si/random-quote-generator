from quote.models import Quote
from django.forms import ModelForm
from django import forms


class AddQuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'quotetype', 'user']
        
    def __init__(self, *args, **kwargs):
        super(AddQuoteForm, self).__init__(*args, **kwargs)
        
        # for field in self.fields.values():
        #     if field.widget.__class__ in  (forms.widgets.TextInput, forms.widgets.Textarea):
        #         field.widget.attrs['class'] = 'quote-text-input'
                
        #         if field.widget.__class__ in  (forms.widgets.Select): # pylint: disable=no-member
        #             field.widget.attrs['class'] += ' quote-select'                
        #         self.fields['quotetype'].widget.attrs['value'] = self.instance.quotetype
        #         self.fields['symbol_text'].widget.attrs['disabled'] = 'disabled'
    