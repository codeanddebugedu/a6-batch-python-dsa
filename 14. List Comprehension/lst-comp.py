# Even from 1 to 10
# [2,4,6,8,10]

# result = [i for i in range(1, 11) if i % 2 == 0]
# print(result)


# Make a list of all prime numbers from 2 to 100
def check_prime(num) -> bool:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


result = [i for i in range(2, 101) if check_prime(i)]
print(result)
