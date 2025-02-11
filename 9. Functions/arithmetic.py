"""
4 functions with 3 required parameters

addition
subtraction
multiply
division a/b/c


a,b,c
"""


def addition(num1: int, num2: int, num3: int):
    print(num1 + num2 + num3)


def subtraction(num1: int, num2: int, num3: int):
    print(num1 - num2 - num3)


def multiply(num1: int, num2: int, num3: int):
    print(num1 * num2 * num3)


def division(num1: int, num2: int, num3: int):
    print(num1 / num2 / num3)


a = int(input("Enter the number 1 = "))
b = int(input("Enter the number 2 = "))
c = int(input("Enter the number 3 = "))
addition(a, b, c)
multiply(a, b, c)
subtraction(a, b, c)
division(a, b, c)
