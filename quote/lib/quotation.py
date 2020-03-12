#import utils as utils
#from utils import utils
from . import utils

class Quotation:
    
    QUOTE_SIMILARITY_RATIO = 0.8
    
    def __init__(self, text=None):
        self.text = text
        
    def __eq__(self, other):
        ''' Assume that 2 quotes are equal if they match more than 80%
        '''
        if isinstance(other, self.__class__):            
           self_words = self.text.split(" ")
           other_words = other.text.split(" ")
           
           if len(self_words) == 0 or len(other_words) == 0:
               return True
           
           other_vocab = set(other_words)
           common_words = [word for word in self_words if word in other_vocab] 
           if len(common_words)/len(self_words) >= self.QUOTE_SIMILARITY_RATIO:
               return True
           
        return False

    def __str__(self):
        return self.text
    


class AdvancedQuotation(Quotation):   
    def __init__(self, *args, **kwargs):   
        super(AdvancedQuotation, self).__init__(*args, **kwargs)
        self.trans_text, self.src_lang = utils.translate(self.text) 

    def __str__(self):
        if self.src_lang == 'en':
            return self.text   
        return self.trans_text +  '(Translated from: ' + self.text + ')'
    
    
