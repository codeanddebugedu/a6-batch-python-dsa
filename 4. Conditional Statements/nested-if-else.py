"""
+ve -> positive
-ve -> Negative
0 -> Zero

Nested If-Else
"""

num = int(input("Enter a number = "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
