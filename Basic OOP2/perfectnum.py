#Task 14

i= int(input())
sum= 0
for s in range(1,i):
    if i%s==0:
        #print(s,end=', ')
        sum+=s
if sum==i: print(i,'is a perfect number')
else: print(i,'is not a perfect number')