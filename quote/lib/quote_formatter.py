import re

class  QuoteFormatter:
    
    MAGIC_WORDS = ['programmer', 'programming']
    
    def beautify(self, quote, key_words=None):
        
        if key_words is None:
            key_words = self.MAGIC_WORDS

        text = str(quote)
        
        def make_strong(match_object):  
            match_group =  match_object.group()         
            return '<strong>' + match_group + '</strong>'

        pattern = '|'.join(key_words)    
        return re.sub(pattern, make_strong, text, flags=re.I)