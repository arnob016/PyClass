l1= input().split()
l2= input().split()

l1.pop(len(l1)-1)
for x in l2:
    l1.append(x)
    
print(l1)
