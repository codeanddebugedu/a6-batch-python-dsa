"""
Make a function, return 'Yes' is a number is even else return 'No'
"""

# def even_odd(num: int) -> str:
#     if num % 2 == 0:
#         return "Yes"
#     else:
#         return "No"


# def even_odd(num: int) -> str:
#     if num % 2 == 0:
#         return "Yes"
#     return "No"


def even_odd(num: int) -> str:
    # Ternary Statement
    return "Yes" if num % 2 == 0 else "No"


print(even_odd(5))
print(even_odd(10))
