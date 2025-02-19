"""
Keep asking chars from the user until he presses Q/q
Enter char = a
Enter char = b
Enter char = c
Enter char = q

abc
"""

result = ""
while True:
    ch = input("Enter a character = ")
    if ch == "q" or ch == "Q":
        break
    result += ch

print(result)
