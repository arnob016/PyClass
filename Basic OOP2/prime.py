#Task 15

i = int(input())

for s in range(2,i):
    if i%s==0:
        print(i,'is not a prime number.')
        break
else: print('is a prime number')