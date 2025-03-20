my_list = [[5, 9, 1, 3, 2], [6, 7, 7, 7, 8], [9, 9, 8, 4, 5]]


rows = len(my_list)
cols = len(my_list[0])


for i in range(0, rows):
    for j in range(0, cols):
        print(my_list[i][j], end=" ")
    print()
