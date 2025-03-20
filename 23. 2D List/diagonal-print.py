my_list = [[5, 9, 8], [4, 6, 7], [3, 2, 1]]

rows = len(my_list)
cols = len(my_list[0])

for i in range(0, rows):
    for j in range(0, cols):
        if j >= i:
            print(my_list[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
