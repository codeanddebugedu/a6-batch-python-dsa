matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # R X C
rows = len(matrix)
cols = len(matrix[0])


for i in range(0, rows - 1):
    for j in range(i + 1, cols):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
