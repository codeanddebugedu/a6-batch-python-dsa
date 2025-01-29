start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start

while i <= end:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1
