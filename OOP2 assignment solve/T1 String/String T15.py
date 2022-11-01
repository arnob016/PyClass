i=0
j=0
k=15
test = '<--cat'
while i < 5:
    k -= 1
    j = k
    while j > 10:
        if j % 2 == 0:
            test += '-->'
            test = test + str(i) + str(j // 2)
        else:
            test += '<--'
            test = test + str(i // 2) + str(j)
        print(test)
        j-=1
    i+=1