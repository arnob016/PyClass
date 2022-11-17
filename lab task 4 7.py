#Suppose you have been given two lists. Write a Python program that replaces the last element of the first list with the second list.
List_one = [1, 4, 7, 5]
List_two = [6, 1, 3,9]

List_one[-1:] = List_two
print (List_one)