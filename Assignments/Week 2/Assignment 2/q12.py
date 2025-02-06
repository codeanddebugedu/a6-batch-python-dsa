# for i in range(5, 0, -1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()
# for i in range(2, 6):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()

n = 9
for i in range(n // 2 + 1, 0, -1):
    for j in range(i, n // 2 + 2):
        print(j, end=" ")
    print()
for i in range(2, n // 2 + 2):
    for j in range(i, n // 2 + 2):
        print(j, end=" ")
    print()
