#Task 23
x = 0
y = 0
sum = 0
p = 0.0
while (x < 10):
    y = x // 2
    while (y < x):
        p = (x + 10.0) / 2
        sum = (sum % 2) + x - y * 2 + int(p)
        print(sum)
        y = y + 2
    if (x > 5):
        x += 1
    else:
        x += 2
#Answer: 6 , 7 , 9 , 5 , 10, 5, 10, 5, 11, 7, 3