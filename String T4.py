word = input()
l=len(word)-1
con = False
dele = 'er'

if word[l]!='t' and word[l-1]!='s' and word[l-2]!='e':


    if word[l]=='r' and word[l-1]=='e':
        con = True
        for x in dele:
            word = word.replace('er','est')
        print(word)

    if con == False:
        if l <= 3:
            print(word)
        elif l >=4 :
            print(word,end='er')
else: print(word)