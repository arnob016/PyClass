word= input()
flagn = True

for n in word:
    if n!='1' and n!='0':
        print('Not a Binary Number')
        flagn = False
        break
    
if flagn is True:
    print('Binary Number')