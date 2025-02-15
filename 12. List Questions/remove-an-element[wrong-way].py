lst = [3, 4, 4, 4, 4, 4, 7, 8]

# n = len(lst)
# for i in range(0, n):
#     if lst[i] == 4:
#         lst.pop(i)

# print(lst)

for num in lst:
    if num == 4:
        lst.remove(num)

print(lst)
