"""
Ask N from user
Ask M from user
Print N to M

n=8
m=12
8 9 10 11 12
"""

n = int(input("Enter n = "))
m = int(input("Enter m = "))

i = n
while i <= m:
    print(i, end=" ")
    i += 1

# while n <= m:
#     print(n, end=" ")
#     n += 1
