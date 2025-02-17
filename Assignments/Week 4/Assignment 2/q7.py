def separate_even_odd(lst):
    """
    Separates even and odd numbers from the original list into two new lists.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    even = []
    odd = []
    n = len(lst)
    for i in range(n):
        if lst[i] % 2 == 0:
            even.append(lst[i])
        else:
            odd.append(lst[i])
    return even, odd


original_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
even_list, odd_list = separate_even_odd(original_list)
print(f"Even = {even_list}")
print(f"Odd = {odd_list}")
