"""
4 functions with 3 required parameters

addition
subtraction
multiply
division a/b/c


a,b,c
"""


def addition(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


def subtraction(num1: int, num2: int, num3: int) -> int:
    return num1 - num2 - num3


def multiply(num1: int, num2: int, num3: int) -> int:
    return num1 * num2 * num3


def division(num1: int, num2: int, num3: int) -> float:
    return num1 / num2 / num3


a = int(input("Enter the number 1 = "))
b = int(input("Enter the number 2 = "))
c = int(input("Enter the number 3 = "))
print(addition(a, b, c))
print(multiply(a, b, c))
print(subtraction(a, b, c))
print(division(a, b, c))
