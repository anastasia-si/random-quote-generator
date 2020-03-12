import re

class  QuoteFormatter:
    """ 
    QuoteFormatter Class -  for quotation formatting
      
    """  
    MAGIC_WORDS = ['programmer', 'programming']
    
    def beautify(self, quote, key_words=None):
        """
        As an example, assume that we need to find specific key words
        in a quotation and highlight them if they exist
        
        Parameters: 
           quote (Quotation): instance of Quotation class
           key_words (List of Strings): list of key words to style, optional
        Returns: 
           string: styled string    
        """
        if key_words is None:
            key_words = self.MAGIC_WORDS

        text = str(quote)
        
        def make_strong(match_object):  
            match_group =  match_object.group()         
            return '<strong>' + match_group + '</strong>'

        pattern = '|'.join(key_words)    
        return re.sub(pattern, make_strong, text, flags=re.I)