# Local Vs Global Variable


def change():
    global a
    a = 100
    b = 200
    print(id(a), id(b))


a = 5
b = 7
print(a, b)
print(id(a), id(b))
change()
print(a, b)
