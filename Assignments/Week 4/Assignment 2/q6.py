def sum_and_average(lst):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    total = sum(lst)  # O(n)
    avg = total / len(lst) if len(lst) != 0 else 0  # O(1)
    print(total)
    print(avg)


sum_and_average([5, 10, 15, 20])
