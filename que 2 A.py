countries = ['India','Thailand','Bhutan','China', 'Nepal', 'Myanmar']

for i in range(len(countries)):
    if countries[i] == 'Myanmar':
        countries.pop(i)

print(countries)