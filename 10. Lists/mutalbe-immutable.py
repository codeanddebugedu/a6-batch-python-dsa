# Immutable
# a = 5
# print(f"ID (a) = {id(a)}")
# print(f"Value (a) = {a}")

# a = 97
# print(f"ID (a) = {id(a)}")
# print(f"Value (a) = {a}")


# Mutable
my_list = [5, 7, 33, 21, 56]
print(f"ID (my_list) = {id(my_list)}")
print(f"Value (my_list) = {my_list}")

my_list[1] = 100
print(f"ID (my_list) = {id(my_list)}")
print(f"Value (my_list) = {my_list}")
