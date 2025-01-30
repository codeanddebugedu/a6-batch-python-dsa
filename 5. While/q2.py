"""
Ask start from user = 3
Ask end from user = 10

Total of all the numbers divisible by 2 and 7
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

total = 0
i = start

while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i += 1

print(total)
