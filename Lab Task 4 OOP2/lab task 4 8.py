#Assume, you have been given two lists. [Your program should work for any two given lists; change the following lists and check whether your program works correctly for the code you have written]
#Write a Python program that creates a new list with all the even elements of both of the given lists and prints the new list.
#You may create a third list to store the even elements of the given lists.

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

list_one = [x for x in list_one if x % 2 == 0]
list_two = [x for x in list_two if x % 2 == 0]
list_one.extend(list_two)
print(list_one)