givendict = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}

maxval = 0
maxkey = ""

for key in givendict:
    if givendict[key] > maxval:
        maxval = givendict[key]
        maxkey = key

print("The highest selling book genre is '" + maxkey + "' and the number of books sold are " + str(maxval) + ".")