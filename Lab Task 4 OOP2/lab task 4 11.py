List_one = [1, 4, 3, 2, 6]
List_two = [5, 6, 9, 8, 7]

flag = True

for x in List_one:
    if x in List_two:
        flag = False
        break
    
print(flag)
