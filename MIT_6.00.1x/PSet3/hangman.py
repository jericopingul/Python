def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    mistakesMade = 0
    
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    print '-------------'
        
    while(mistakesMade < 8):
        availableLetters = getAvailableLetters(lettersGuessed)

        print 'You have ' + str(8 - mistakesMade) + ' guesses left.'
        print 'Available letters: ' + availableLetters
        guess = str(raw_input('Please guess a letter: '))
        
        if(guess in availableLetters and guess not in lettersGuessed):
            lettersGuessed += guess
            guessedWord = getGuessedWord(secretWord,lettersGuessed)

            if(guess in secretWord):
                print 'Good guess: ' + guessedWord
            else:
                print '	Oops! That letter is not in my word: ' + guessedWord
                mistakesMade += 1  
            print '-------------'

            if(isWordGuessed(secretWord,lettersGuessed)):
                print 'Congratulations, you won!'
                break 
        else:
            print 'Oops! You\'ve already guessed that letter: ' + guessedWord
            print '-------------'

                
    if(mistakesMade == 8):
        print 'Sorry, you ran out of guesses. The word was ' + secretWord


