"""
if index is Even -> +1
if index is Odd -> -1
"""

my_list = [5, 7, 33, 21, 56, 38, 76, 12, 12, 33, 33, 97]
print(my_list)
n = len(my_list)


for i in range(0, n):
    if i % 2 == 0:
        my_list[i] += 1
    else:
        my_list[i] -= 1

print(my_list)
