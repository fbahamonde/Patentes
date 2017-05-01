import re, string

def remove_punctuation ( text ):
    temp=re.sub('[%s]' % re.escape(string.punctuation), ' ', text)[1:-3]
    text = temp[:5] + ' ' + temp[6:]
    return text
    
        

