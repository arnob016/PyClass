#Task 4

n=s=0
while True:
    if n>600: break
    
    n += 1
    if n%7==0 and n%9==0:
        s=s
        
    elif n%7==0 or n%9==0:
        s=s+n
#    print(s,n)    
print(s)