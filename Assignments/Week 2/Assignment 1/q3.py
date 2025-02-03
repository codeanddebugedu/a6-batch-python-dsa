n = int(input("Enter a number = "))

# Method 1
"""
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)
"""


# Method 2
"""
count = 1
for i in range(1, n // 2 + 1):
    if n % i == 0:
        count += 1
print(count)
"""


# Method 3
count = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        count += 1
        if n // i != i:
            count += 1
print(count)
