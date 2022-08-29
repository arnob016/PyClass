#Task 13

i= int(input())
n=1
for s in range(1,i):
    if i%s==0:
        print(s,end=', ')
        n+=1
print(i)
print(f'Total {n} divisors.')