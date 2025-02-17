"""
Write a Python code to check if a list is a palindrome 
(reads the same forwards and backwards). Just print “YES” or “NO”

Time Complexity - O(n)
Because we are iterating only once.

Space Complexity - O(1)
"""

from typing import List


def isPalindrome(lst: List) -> bool:
    n = len(lst)
    for i in range(0, n):
        if lst[i] != lst[n - i - 1]:
            return False
    return True


print(isPalindrome([1, 2, 3, 4, 4, 3, 2, 1]))
print(isPalindrome([1, 2, 3, 4, 3, 2, 1]))
print(isPalindrome([1, 2, 3, 4, 3, 4, 1]))
