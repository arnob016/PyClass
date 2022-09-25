word= input()
n = int(input())
m = n+1
j= len(word)
while n>=0:
    print(word[n],end='')
    n -= 1

while True:
    print(word[m],end='')
    m += 1
    if m>=j: break