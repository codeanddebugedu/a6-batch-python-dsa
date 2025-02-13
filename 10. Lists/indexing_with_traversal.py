my_list = [5, 7, 33, 21, 56, 38, 76]

n = len(my_list)
# print(n)

# for i in range(0, n):
#     print(my_list[i])

# Reverse print
for i in range(n - 1, -1, -1):
    print(my_list[i], end=" ")
