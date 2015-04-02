def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    score = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None
      

    # For each word in the wordList
    for wordIndex in range(len(wordList)):
        if(isValidWord(wordList[wordIndex], hand, wordList)):
            score = getWordScore(wordList[wordIndex], n)
            if(maxScore < score):
                maxScore = score
                bestWord = wordList[wordIndex]
    return bestWord