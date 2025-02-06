"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""

# for i in range(5, 0, -1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()

n = 5
for i in range(n, 0, -1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
