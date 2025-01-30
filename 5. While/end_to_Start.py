"""
Ask start from user = 15
Ask end from user = 3

15 14 13 12 11 10 9 8 7 6 5 4 3
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start

while i >= end:
    print(i, end=" ")
    i -= 1
