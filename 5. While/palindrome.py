"""
Ask a number = 8563
"""

num = int(input("Enter a number = "))
n = num
ans = 0
while n > 0:
    ld = n % 10
    ans = (ans * 10) + ld
    n = n // 10

if ans == num:
    print("Yes")
else:
    print("No")
