list1= list(map(int,input().split()))

if len(list1)<2:
    print("Not enough elements")
else:
    list1.pop(0)
    list1.pop(len(list1)-1)
    print(list1)