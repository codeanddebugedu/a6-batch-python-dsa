"""
Write a Python code to check if a given list is sorted in ascending order.
Time Complexity - O(n)
Because we are iterating only once.

Space Complexity - O(1)
"""

from typing import List


def isSorted(lst: List[int]) -> bool:
    n = len(lst)
    for i in range(0, n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


print(isSorted([1, 3, 4, 5, 6, 12, 19]))
print(isSorted([22, 3, 4, 5, 6, 12, 19]))
