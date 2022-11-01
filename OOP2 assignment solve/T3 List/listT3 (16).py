s = []
for n in range (5):
    s.append(int(input()))
print('Input data:',s)
s2 = []
for m in range(5):

    s2.append(s[4-m])
print('Printing values in reverse order:')
for x in s2:
    print(x)
