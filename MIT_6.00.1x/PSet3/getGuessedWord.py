def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    sWordList = [] # create list
    for i in secretWord:
        sWordList += '_'
     
    for letter in lettersGuessed:   
        for ind in range(len(secretWord)):
            if(secretWord[ind] == letter):
                sWordList[ind] = letter
    # convert to string
    sWordStr = ''
    for l in sWordList:
        sWordStr += l  
        if (l == '_'):
            sWordStr += ' '            
                     
    return sWordStr