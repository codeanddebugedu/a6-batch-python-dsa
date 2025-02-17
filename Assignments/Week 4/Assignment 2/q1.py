def create_user_list():
    """
    Time Complexity: O(n)
    Space Complexity: O(1) because nums is our answer
    """
    total_elements = int(input("Enter number of elements = "))
    nums = []
    for _ in range(total_elements):
        num = int(input("Enter number = "))
        nums.append(num)
    return nums


print(create_user_list())


# Alternate Solution

# def create_user_list():
#     """
#     Time Complexity: O(n)
#     Space Complexity: O(1)
#     """
#     total_elements = int(input("Enter number of elements: "))
#     nums = [int(input("Enter number: ")) for _ in range(total_elements)]
#     return nums


# print(create_user_list())
