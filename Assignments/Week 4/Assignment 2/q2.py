def remove_duplicates(user_list):
    """
    Time Complexity: O(n*n) -> O(n^2)
    Space Complexity: O(1)
    """

    result = []
    for num in user_list:  # O(n)
        if num not in result:  # O(n)
            result.append(num)  # O(1)

    return result


user_list = []
for _ in range(10):
    num = int(input("Enter number = "))
    user_list.append(num)


print(remove_duplicates(user_list))
