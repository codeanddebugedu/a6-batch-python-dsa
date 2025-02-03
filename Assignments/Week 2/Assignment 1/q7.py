n = int(input("Enter a number = "))
while n >= 10:
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    n = sum_of_digits
print(n)


# Method 2
# n = int(input("Enter a number = "))
# while n >= 10:
#     n = n % 10 + n // 10
# print(n)
