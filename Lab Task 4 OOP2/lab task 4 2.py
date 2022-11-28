inplist = []
inp = list( map(int,input().split(',')))
if len(inp)<4:
    print('Not Possible')
else:
    print ( inp[2:-2] )
