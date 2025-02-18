"""
What is a lambda function?

Anonymous function - one liners
"""

# def addition(a, b):
#     return a + b

# def check_even(num):
#     return "Yes" if num % 2 == 0 else "No"


addition = lambda a, b: a + b
check_even = lambda num: "Yes" if num % 2 == 0 else "No"


x = addition(5, 10)
print(x)

print(check_even(10))
