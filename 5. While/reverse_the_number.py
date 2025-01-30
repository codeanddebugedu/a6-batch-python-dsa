"""
Ask a number = 8563
3658
"""

num = int(input("Enter a number = "))
ans = 0
while n > 0:
    ld = n % 10
    ans = (ans * 10) + ld
    n = n // 10
print(ans)
