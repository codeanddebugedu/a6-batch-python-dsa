def sum_lists(list1, list2):
    """
    Time Complexity: O(n)
    Because both the list have same length that is N
    And we are iterating N times only

    Space Complexity: O(1)
    Dont consider result, as its our answer
    """
    n = len(list1)
    result = []
    for i in range(0, n):
        result.append(list1[i] + list2[i])
    return result


print(sum_lists([1, 2, 3], [4, 5, 6]))
