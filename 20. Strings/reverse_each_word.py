"""
we are learning python with dsa
ew era gninrael ....
"""

string = "we are learning python with dsa"
words = string.split()
print(words)

result = " ".join(w[::-1] for w in words)
print(result)
