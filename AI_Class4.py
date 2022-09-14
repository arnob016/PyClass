Games= ('Football', 'Cricket', 'Tennis','Football', 'Rugby', 'Basketball', 'Football', 'Archery', 'Cricket')
(Messi, Sakib, Novak, *Others) = Games
Names=Games
List_G=[Messi, Sakib, Novak]

print('Unpacked items: ',List_G)
print('Rest items: ',*Others)

list1=[]

for i in Games:
    list1.append(i)
print(list1)

list2=list1
n=0
print('For List: ')
for i in list1:
    n=0
    for j in list2:
        if i==j :
            n+=1
            if n>=2:
                print(i,'is duplicate',n,'times')
            
print('For Tuple: ') 
for x in Games:
    z=0
    for y in Names:
        if x==y :
            z+=1
            if z>=2:
                print(x,'is duplicate',z,'times')