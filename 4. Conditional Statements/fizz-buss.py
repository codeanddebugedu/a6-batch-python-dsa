"""
Ask a number from user

if number divisible by 2 -> FIZZ
if number divisible by 3 -> BUZZ
if number divisible by 2 and 3 -> FIZZBUZZ
else:
FIZZFIZZBUZZBUZZ
"""

num = int(input("Enter a number = "))
if num % 2 == 0 and num % 3 == 0:
    print("FIZZBUZZ")
elif num % 2 == 0:
    print("FIZZ")
elif num % 3 == 0:
    print("BUZZ")
else:
    print("FIZZFIZZBUZZBUZZ")
