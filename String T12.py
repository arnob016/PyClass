test = ""
i = 0
j = 0
k = 15
test = "-->"
while i < 5:
    j = k - 1
    k -= 1
    while j > 10:
        test = str(i + j) + "-->" + test
        print(test)
        j -= 1
    i += 1
