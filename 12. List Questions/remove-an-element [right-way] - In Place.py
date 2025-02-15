lst = [3, 4, 4, 4, 4, 4, 7, 8, 5, 4, 34, 4, 4, 4, 4, 4]

while True:
    if 4 in lst:
        lst.remove(4)
    else:
        break

print(lst)
