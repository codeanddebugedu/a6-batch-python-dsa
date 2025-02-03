n = int(input("Enter a number = "))

# Method 1
"""
total_sum = 0
for i in range(1, n + 1):
    if n % i == 0:
        total_sum += i
print(total_sum)
"""


# Method 2
"""
total_sum = n
for i in range(1, n // 2 + 1):
    if n % i == 0:
        total_sum += i
print(total_sum)
"""


# Method 3
total_sum = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        total_sum += i
        if n // i != i:
            total_sum += n // i
print(total_sum)
