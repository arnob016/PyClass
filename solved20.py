#Task 20
x = 0 
p =0 
sum = 0 
p = 1 
x = 2 
q = None 
sum = 0 
while p < 12: 
    q = x + p - (sum + 7 / 3) / 3.0 % 2 
    sum = sum + x + int(q) 
    x += 1 
    print(sum) 
    if x > 5: 
        p += 4 / 2 
    else: 
        p += (3 % 1) 
sum = int(sum + p) 
print(sum) 
#Answer : 4, 10, 18, 28, 42, 60, 82, 108, 138, 151