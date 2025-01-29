start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
n = int(input("Enter a number = "))

i = start

while i <= end:
    if i % n == 0:
        print(i, end=" ")
    i += 1
