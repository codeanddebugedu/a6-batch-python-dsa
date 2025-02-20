"""
Lower case to Upper case
"""

string = "dhdkjwAKDHGWA36478326^&*$^#*dwjahkdhYDGHAKJDwh"
result = ""


for ch in string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        new_ascii = ascii_code - 32
        new_ch = chr(new_ascii)
        result += new_ch
    else:
        result += ch

print(result)
