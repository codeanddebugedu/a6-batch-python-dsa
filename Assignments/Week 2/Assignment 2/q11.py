"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# for i in range(4, -1, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

n = 9
for i in range(1, n // 2 + 2):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(n // 2, -1, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
