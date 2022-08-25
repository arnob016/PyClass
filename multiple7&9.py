n=s=0
while True:
    if n>600: break
    n += 1
    if n%7==0 and n%9==0:
        s=s+n
print(s)