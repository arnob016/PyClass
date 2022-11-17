#Task 8

n= int(input())
k=0
sum=0
while True:
    k+=1
    j=7*k
    if n<j: break
#    print(n,k,j,sum)
    sum= sum+j
print(sum)
    