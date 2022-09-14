list1=[]
print('Input the list elements: ')

for i in range(6):
    list1.append(input())
    
Value= input('Input what you want to search:\n')

if Value in list1[3:5]: 
    print(f'{Value} is on the list')
else:
    print(f'{Value} is not on the list')