"""
Find factors - Brute Force Solution
Enter a number = 20
1 2 4 5 10 20
"""

num = int(input("Enter a number = "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
