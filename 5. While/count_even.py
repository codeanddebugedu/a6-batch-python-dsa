"""
Count the number of digits divisible by 3 and 5 between 1 to 100
"""

i = 1
count = 0
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        count += 1
    i += 1

print(count)
