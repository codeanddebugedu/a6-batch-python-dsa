# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(2, end=" ")
#         else:
#             print(1, end=" ")
#     print()

# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(2, end=" ")
#         else:
#             print(1, end=" ")
#     print()

n = 9
for i in range(1, n // 2 + 1 + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()
