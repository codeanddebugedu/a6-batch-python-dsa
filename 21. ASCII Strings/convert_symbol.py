"""
string = "ani$#%ru dh23"
string = "ani---ru dh23"
"""

string = "ani$#%ru dh23"
result = ""

for ch in string:
    ascii_code = ord(ch)
    if (
        (ascii_code >= 97 and ascii_code <= 122)
        or (ascii_code >= 65 and ascii_code <= 90)
        or (ascii_code >= 48 and ascii_code <= 57)
        or ascii_code == 32
    ):
        result += ch
    else:
        result += "-"

print(result)
