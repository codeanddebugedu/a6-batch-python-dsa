"""
Ask N from user = 
Sum of 1 to N
"""

n = int(input("Enter N = "))

total = 0
i = 1
while i <= n:
    total = total + i
    i += 1

print(total)
