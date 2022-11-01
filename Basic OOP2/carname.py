#Task 2

carname= str(input())
while True:
    try:
        num = int(input())
        break
    except: print("Only input an integer please.")
for n in range(num):
    print(carname)
