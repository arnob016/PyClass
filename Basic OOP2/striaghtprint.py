#Task 12

n=0
num =  int(input())
num2 = num
while True:
    n+=1
    num /=10
    if num<10:
        n=n+1
        break
    

x= n

while True:
    x -= 1
    print(int(num2/(10**x)), end=', ')
    num2%=(10**x)
    if num2<10:
        break

print(num2)

