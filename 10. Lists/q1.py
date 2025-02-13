# Print all even numbers

my_list = [5, 7, 33, 21, 56, 38, 76, 12, 12, 33, 33]
n = len(my_list)

for i in range(0, n):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=" ")
