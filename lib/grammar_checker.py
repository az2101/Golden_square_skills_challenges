
def grammar_checker(text):
    punctuation = '?!.'
    if text[0].isupper():
        if text[-1] in punctuation:
            return True
    return False
  
    
    

