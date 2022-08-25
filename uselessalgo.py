#Task 10

n= int(input())

while True:
    print(int(n%10), end=', ')
    n/=10
    if n<=10 or n%10==0:
        break
print(int(n))