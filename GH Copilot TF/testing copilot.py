#The first line of the input contains a single integer N (1 ≤ N ≤ 1000), indicating the number of test cases. Each test case contains a single floating-point number X (1 ≤ X ≤ 1000), indicating the amount of food available for Blobs.
#For each test case, print one line containing the number of days that blobs will take to eat all their food supply, followed by the word "dias" that means days in portuguese.

# Sample Input 1
#3
#40.0
#200.0
#300.0

# Sample Output 1
#6 dias
#8 dias
#9 dias

def main():
    n = int(input())
    for i in range(n):
        x = float(input())
        print(int(x / 2), "dias")
    
if __name__ == "__main__":
    main()
    
