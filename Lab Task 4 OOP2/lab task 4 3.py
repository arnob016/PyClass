list1= []
while True:
    i = int(input())
    list1.append(i)
    if i == 0:
        break
    
print('Input data:',list1,)
print('Printing values from the list in reverse order:')
k = len(list1)-1
for j in range(k):
    print(list1[k-j])
    
