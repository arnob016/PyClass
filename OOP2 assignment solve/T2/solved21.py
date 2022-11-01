#Task 21
x = 0 
p = 0 
sum = 0 
p = 1 
x = 2 
q = 0.0 
sum = 0 
while (p < 10) : 
    q = x + p - (sum + int(5 / 3)) / 3.0 % 2 
    sum = sum + x + int(q) 
    x += 1 
    print(sum) 
    if (x > 5) :
        p += int(4 / 2) 
    else : 
        p += 3 % 1 
sum = sum + p 
print(sum)
#Answer: 4 , 9 , 16, 25, 39, 56, 78, 104, 115