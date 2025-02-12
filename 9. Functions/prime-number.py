"""
Ask a integer as a parameter


Return True if that number is prime else print False
"""


def check_prime(num: int) -> bool:
    # num = 10
    # 2 to 9
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(check_prime(7))
print(check_prime(10))
