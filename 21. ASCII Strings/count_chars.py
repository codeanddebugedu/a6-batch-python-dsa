"""
Ask input
Lower = 
Upper = 
Digit = 
Space = 
Symbol = 
"""

s = "ANIruDh ^* KHUrana"

lowercase_count = 0
uppercase_count = 0
digit_count = 0
space_count = 0
symbol_count = 0

for ch in s:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        lowercase_count += 1
    elif ascii_code >= 65 and ascii_code <= 90:
        uppercase_count += 1
    elif ascii_code >= 48 and ascii_code <= 57:
        digit_count += 1
    elif ascii_code == 32:
        space_count += 1
    else:
        symbol_count += 1

print(f"Lower case = {lowercase_count}")
print(f"Upper case = {uppercase_count}")
print(f"digit_count = {digit_count}")
print(f"space_count = {space_count}")
print(f"symbol_count = {symbol_count}")
