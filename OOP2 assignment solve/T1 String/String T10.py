a,b = input().split(', ')
word = ''
addr = ''

if len(a)>len(b):
    x = a
    y = b
else:
    x = b
    y = a

y += '$'*(len(x) - len(y))

    
for n in range(len(x)):
    if a==x:
        addr = x[n] + y[n]
    elif b==x: 
        addr = y[n] + x[n]
    word += addr
   


word= word.replace('$', '')
print(word)