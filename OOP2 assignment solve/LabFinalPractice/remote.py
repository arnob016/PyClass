while True:
    a,b = map(int, input().split())
     
    if a == -1 and b == -1 :
        break
    
    print(min(abs(a-b), 100-abs(a-b)))