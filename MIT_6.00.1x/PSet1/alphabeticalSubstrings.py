count = 1
word = s[0]
wordcount = 0
l_count = 0

for i in range(1, len(s)):
    if(s[i] >= s[i-1]):
        word = word + s[i]
        count += 1
        if(i == (len(s) - 1)  and count > l_count):
            l_word = word
    else:
        wordcount += 1
        if(wordcount == 1):
            l_word = word
            l_count = count
            count = 1
            word = s[i]
        elif(count > l_count):
            l_word = word
            l_count = count
            count = 1
            word = s[i]
        else:
            count = 1
            word = s[i]        
        
print 'Longest substring in alphabetical order is: ' + l_word