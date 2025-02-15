lst = [3, 4, 4, 4, 4, 4, 7, 8, 5, 4, 34, 4, 4, 4, 4, 4]
result = []


for i in range(0, len(lst)):
    if lst[i] not in result:
        result.append(lst[i])

print(result)
