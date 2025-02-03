n = int(input("Enter a number = "))

# Method 1
"""
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
"""

# Method 2
"""
for i in range(1, n // 2 + 1):
    if n % i == 0:
        print(i, end=" ")
print(n)
"""


# Method 3
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        print(i, end=" ")
        if n // i != i:
            print(n // i, end=" ")
