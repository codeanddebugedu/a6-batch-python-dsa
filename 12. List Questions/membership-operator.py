"""
BOOLEAN
IN
NOT IN 
In case of a list - O(N)
"""

lst = [3, 4, 4, 4, 4, 4, 7, 8, 5, 4, 34, 4, 4, 4, 4, 4]

x = 77
if x not in lst:
    print("No")
else:
    print("Yes")
