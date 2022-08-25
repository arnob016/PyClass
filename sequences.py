#Task 1 : 

# a)  24, 18, 12, 6, 0, -6 

a = 24
print('a)', end= ' ')

for s in range(6):
    print(a, end=' ')
    a -= 6
print()

# b)  24, 18, 12, 6, 0, -6 

b= -10
print('b)',end=' ')

for s in range(7):
    print(b, end=' ')
    b += 5
print()

# c) 18, 27, 36, 45, 54, 63 

c = 18
print('a)', end= ' ')

for s in range(6):
    print(c, end=' ')
    c += 9
print()

# d) 18, -27, 36, -45, 54, -63 

d= 18
print('b)',end=' ')

for s in range(6):
    print(d, end=' ')
    d = d*-1
    if d>0: d += 9
    if d<0: d -= 9