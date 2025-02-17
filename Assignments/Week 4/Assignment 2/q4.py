# Q4: Remove the nth index element from a list using a function.


def remove_nth_element(lst, index):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    n = len(lst)
    if 0 <= index < n:
        # del lst[n]
        lst.pop(index)
    return lst


print(remove_nth_element([10, 20, 30, 40, 50], 2))
