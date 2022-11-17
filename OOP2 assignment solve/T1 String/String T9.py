word= input()+' '
word2=''
for n in range(len(word)):
    if ord(word[n]) != ord(word[n-1]):
        word2 += word[n]

print(word2)