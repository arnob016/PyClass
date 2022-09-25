test = ""
i = 5
j = 0
k = 15
while (i< 10):
    k-=1
    j = k
    while (j > 10 ):
        if j % 2 == 0:
            test = "<--"
            test = test + str( i) + '3' + "-->" + str(j // 3)
        else:
            test = "-->"
            test = "-->" + str((i // 3)) + test + str(j)
        print(test)
        j -=1
    i+=1

