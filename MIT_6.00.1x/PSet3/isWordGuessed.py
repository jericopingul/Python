def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    sWordList = []
    for i in secretWord:
        sWordList += i
    for letter in lettersGuessed:
        if(letter in sWordList):
            sWordList.remove(letter)
    return len(sWordList) == 0