i = 10
while(i >= -20):
    if(i < 0):
        test = " != "
        test = str(i//2) + test + str(int(i/2))
    else:
        test = " == "
        test = str(i//2) + test + str(int(i/2))
        print(test)
    i -= 5