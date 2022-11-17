#Sample Input 2:
#7, 7, 7, 1, 0, 3, 3, 55, 9
#Sample Output 2:
#Input list: [7, 7, 7, 1, 0, 3, 3, 55, 9]
#Modified list: [7, 1, 0, 3, 55, 9]

list_D = [int(x) for x in input('Enter the list of numbers separated by commas: ').split(',')] 
print('Input list: ', list_D)
list_A =[]


for x in list_D:
    if x not in list_A:
        list_A.append(x)

print('Modified list: ',list_A)