#Task 7

z=sum=0
for n in range(10):
    x= int(input())
    if x%2!=0:
        sum += x
        z+=1
print(sum/z)