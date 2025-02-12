"""
Make a function, return True is a number is even else return Odd
"""

# def even_odd(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# def even_odd(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     return False


def even_odd(num: int) -> bool:
    return num % 2 == 0


print(even_odd(5))
print(even_odd(10))
