List1= [1,2,3]
List2= [5,6,7]

print('Extending list')
List1.extend(List2)
print(List1)

List1.insert(3,4)
print('Inserting into list')
print(List1)

Tuple_n=(8, 9)
print('Tuple into list')
List1.extend(Tuple_n)
print(List1)