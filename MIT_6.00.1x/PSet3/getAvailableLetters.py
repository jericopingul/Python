def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  
    a = []       
    for letter in alphabet:
        a += letter  
              
    alphabet = ''
    
    for l in lettersGuessed:
        if(l in a):
            a.remove(l)
            
    for ind in range(len(a)):
        alphabet += a[ind]
    return alphabet