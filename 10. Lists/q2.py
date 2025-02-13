# Print all the prime numbers in the list


def check_prime(num) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [5, 7, 33, 21, 56, 38, 76, 12, 12, 33, 33, 97]
n = len(my_list)
for i in range(0, n):
    if check_prime(my_list[i]):
        print(my_list[i], end=" ")
