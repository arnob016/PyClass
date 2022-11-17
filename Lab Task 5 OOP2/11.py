input_string = input()

dict1 = {}

for i in input_string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)