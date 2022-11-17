list1= []
list2=[]
for i in range(1,4):
    list1.append(-i)
    list2.append(i)
print(f'{list1}\n{list2}')

sum1=0
sum2=0

for s in list1:
        sum1 += s
    
for x in list2 :
    sum2 += x

print(f'Sum for negative list: {sum1}\nSum for positive list: {sum2}')
        