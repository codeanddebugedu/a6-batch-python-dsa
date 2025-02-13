# Print sum of all the numbers

my_list = [5, 7, 33, 21, 56, 38, 76, 12, 12, 33, 33]
n = len(my_list)

total = 0

for i in range(0, n):
    total = total + my_list[i]

print(total)
