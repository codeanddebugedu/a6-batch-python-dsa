start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

even_count = 0
odd_count = 0

i = start
while i <= end:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print(f"Even = {even_count}")
print(f"Odd = {odd_count}")
