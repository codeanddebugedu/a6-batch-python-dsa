def remove_even_numbers(user_list):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    result = []
    for num in user_list:  # O(n)
        if num % 2 != 0:  # O(1)
            result.append(num)  # O(1)

    return result


user_list = []
for _ in range(10):
    num = int(input("Enter number = "))
    user_list.append(num)


print(remove_even_numbers(user_list))
