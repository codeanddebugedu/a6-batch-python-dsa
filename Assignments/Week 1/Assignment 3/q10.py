start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

if start > end:
    temp = start
    start = end
    end = temp

i = start

while i <= end:
    print(i, end=" ")
    i += 1
