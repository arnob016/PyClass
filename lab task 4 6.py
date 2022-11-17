def iambigger(a,b):
    if a>b:
        return a
    if b>a:
        return b
list1 = list(map(int,input().split(',')))
v=-124612325515123
for i in list1:
    c=i
    v= iambigger(c,v)
print('My list:', list1)
print('Largest number in the list is',v, 'which was found at index', 1+list1.index(v))