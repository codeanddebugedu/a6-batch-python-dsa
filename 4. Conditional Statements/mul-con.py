"""
Print Yes
if number is divisible by 2 and 3
but should not be divisible by 5

No
"""

num = int(input("Enter a number = "))

if num % 2 == 0 and num % 3 == 0 and num % 5 != 0:
    print("yes")
else:
    print("no")
