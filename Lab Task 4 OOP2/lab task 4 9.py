#Write a Python program that reads a string as an input from the user where multiple numbers are separated by spaces. Then, make a list of numbers from the input string without using the split() function and print the list. Finally, remove all the occurrences of even numbers from the same input list and print the modified list.

#Sample Input:
#7 12 4 55 96 2 11 61 33 42
#Sample Output:
#Original list: [7, 12, 4, 55, 96, 2, 11, 61, 33, 42]
#Modified list: [7, 55, 11, 61, 33]
listn = [int(x) for x in input('Enter the list of numbers separated by space: ').split()] 
print('Original list: ', listn)
listn = [x for x in listn if x%2 != 0]
print('Modified list: ', listn)
