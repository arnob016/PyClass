#Sample 1
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}

dict3 = {**dict1, **dict2}
print(dict3)

#Sample 2
dict1 = {'A':90, 'B': 0}
dict2 = {'C':50}

dict3 = {**dict1, **dict2}
print(dict3)