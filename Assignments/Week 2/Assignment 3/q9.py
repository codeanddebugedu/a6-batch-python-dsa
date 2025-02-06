n = 5
num = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(num, num + i):
            print(j, end=" ")
        num += i
    else:
        for j in range(num + i - 1, num - 1, -1):
            print(j, end=" ")
        num += i
    print()