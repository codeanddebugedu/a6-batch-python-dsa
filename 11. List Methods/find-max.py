# def find_max_number(nums: list):
#     n = len(nums)
#     maxi = float("-inf")
#     for i in range(0, n):
#         if nums[i] > maxi:
#             maxi = nums[i]
#     return maxi
#     # return max(nums)


def find_max_number(nums: list):
    n = len(nums)
    maxi = float("-inf")
    for i in range(0, n):
        maxi = max(maxi, nums[i])
    return maxi
    # return max(nums)


my_list = [54, 74, 85, 41, 52, 33, 68, 55, 66]
print(find_max_number(my_list))
