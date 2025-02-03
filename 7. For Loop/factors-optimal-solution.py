num = int(input("Enter a number = "))

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        print(i, end=" ")
        if num // i != i:
            print(num // i, end=" ")
