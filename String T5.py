word = input()

n= 0

for x in range (0,len(word)-1):
    for y in range(0,x+1):
        print(word[y],end='')   
    print()
print(word)
