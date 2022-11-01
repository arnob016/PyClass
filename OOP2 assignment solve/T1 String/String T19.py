word = input().lower()
new_word = []
for s in range(len(word)-1):
    new_word.append(word[s])

new = []
for n in range(len(new_word)+1):
    if word[n] == ' ' :
        n -= 1
        new.append(' ')

    elif n%2==0 or n==0:
        k = word[n].upper()
        new.append(k)
         
    elif n%2!=0 and n!=0:
        new.append(word[n])
        
for l in new:
    print(l, end='')