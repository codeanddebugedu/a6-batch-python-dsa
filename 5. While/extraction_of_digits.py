"""
Extraction of digits

Ask a number = 23453
2 3 4 5 3
3 5 4 3 2
"""

num = int(input("Enter a number = "))
n = num
while n > 0:
    ld = n % 10
    print(ld, end=" ")
    n = n // 10
