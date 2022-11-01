string = input()
count = 0
list1 = []
list2 = []
for n in string:
    list1.append(n)
    
list1.sort()
k= len(list1)-1
for x in range (k):
    count=0
    if k<x: break
    for y in range (k):
        if k<y: break
        print(x,y)
        if x!=y and list1[x] == list1[y]:
            count +=1
            list1.pop(y)
            k = k-1
            print(list1, list2)
    list2.append(count)

for nu in range(len(list1)):
    print(list1[nu],' ',list2[nu])
