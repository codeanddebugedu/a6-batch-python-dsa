matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # R X C
rows = len(matrix)
cols = len(matrix[0])


# C x R
result = [[0 for _ in range(cols)] for _ in range(rows)]
# print(result)


for i in range(0, rows):
    for j in range(0, cols):
        result[j][i] = matrix[i][j]

print(result)
