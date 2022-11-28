
myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index1 = 0
index2 = 0
index1 = 1
while(index1<10):
    myList[index1] = index1+4
    index2 = 1
    while(index2<index1):
        myList[index1] = myList[index1] + myList[index2]-index1
        index2 = index2+1
    print(myList[index1])
    index1 = index1+1

