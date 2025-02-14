from copy import deepcopy

a = [43, 1, 3, [5, 6, 7, 5], 4, 3, 45, 65, 6]


b = deepcopy(a)

print(f"a = {a}")
print(f"b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

b[3][1] = 100
print(f"a = {a}")
print(f"b = {b}")
