#Task 16

num= int(input())
sum=0
maxnum=-111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
minnum=111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
for s in range(0,num):
    i=int(input())
    if i>maxnum:
        maxnum= i
    if i<minnum:
        minnum= i
    sum+= i
avg= sum/num
print('Maxinum',maxnum)
print('Mininum',minnum)
print('Average is',avg)