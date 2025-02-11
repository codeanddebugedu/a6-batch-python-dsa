# Pass by value (int,str,floats, tuples)
# Pass by reference (address) (list, dictionaries, sets)


def change(a, b, c):
    a = 100
    b = 100
    c = 100


a = 3
b = 2
c = 1
print(a, b, c)
change(a, b, c)
print(a, b, c)
