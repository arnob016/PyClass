list1= list(map(int,input('First List: ').split()))
list2= list(map(int,input('Second List: ').split()))
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)

print (list3)