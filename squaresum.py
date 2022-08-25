#Task 6

n= int(input())
x=0

for s in range(1,n+1):
    sqr=s**2
    if sqr%2!=0:
        x+= sqr
    else: x-= sqr
#    print(s,sqr,x)
print(x)