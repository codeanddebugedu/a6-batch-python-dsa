start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

total_sum = 0

i = start
while i <= end:
    total_sum += i
    i += 1

print(f"Total sum from {start} to {end} is {total_sum}")
