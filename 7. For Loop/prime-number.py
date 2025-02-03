"""
Ask a number = 


Yes
No
"""

num = int(input("Enter a number = "))
count = 0

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        count += 1
        if num // i != i:
            count += 1
            if count > 2:
                break

if count == 2:
    print("Yes, it is a prime number")
else:
    print("No, it is not a prime number")
