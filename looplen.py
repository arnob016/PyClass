#Task 11

n=0
num =  int(input())
while True:
    n+=1
    num /=10
    if num<10:
        n=n+1
        break
    
print(n)