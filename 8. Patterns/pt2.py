"""
n = 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

n = 3
1 2 3
1 2 3
1 2 3
"""

n = 7
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
