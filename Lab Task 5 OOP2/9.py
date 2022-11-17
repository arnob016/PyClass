userinpt= input()

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}

newdict = {}

for i in exam_marks:
    if exam_marks[i] >= int(userinpt):
        newdict[i] = exam_marks[i]

print(newdict)