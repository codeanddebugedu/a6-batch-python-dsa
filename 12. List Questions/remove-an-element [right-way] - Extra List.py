lst = [3, 4, 4, 4, 4, 4, 7, 8, 5, 4, 34, 4, 4, 4, 4, 4]
result = []
n = len(lst)

for i in range(0, n):
    if lst[i] != 4:
        result.append(lst[i])


print(result)
