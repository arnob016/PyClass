#Task 27

bin= int(input())
x=1
dec=0
l= len(str(bin))

for s in range(l):
    r= bin%10
    dec = dec + (r*x)
    x = x*2
    bin = int(bin/10)
    #print(dec)
print(dec)