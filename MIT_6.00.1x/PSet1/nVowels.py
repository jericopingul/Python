count = 0

for i in range(0, len(s)):
    if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        count += 1
        
print 'Number of vowels: ' + str(count)