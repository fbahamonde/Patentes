import re, string

def remove_punctuation ( text ):
    temp=re.sub('[%s]' % re.escape(string.punctuation), ' ', text)[1:-3]
    if temp[0]!=' ' and temp[1]!=' ' and temp[3]!=' ' and temp[4]!=' ' and temp[6]!=' ' and temp[7]!=' ':
        temp = temp[:2] + ' ' + temp[3:]
        temp = temp[:5] + ' ' + temp[6:]
        return temp
    if len(temp)==7:
        if temp[2]!=' ':
            temp = temp[:2] + ' ' + temp[2:]
        if temp[5]!=' ':
            temp = temp[:5] + ' ' + temp[5:]
    return temp
    
        

