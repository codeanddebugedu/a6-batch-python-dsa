# Return a list of all unique elements (Order doesnt matter)

# my_list = [5, 6, 4, 4, 3, 2, 5, 2, 1, 2, 2, 5, 6]
# my_set = set()

# for i in range(0, len(my_list)):
#     my_set.add(my_list[i])

# print(my_set)
# result = []
# for num in my_set:
#     result.append(num)
# print(result)

# Return a list of all unique elements (Order matters)

my_list = [5, 6, 4, 4, 3, 2, 5, 2, 1, 2, 2, 5, 6]
my_dict = dict()

for i in range(0, len(my_list)):
    my_dict[my_list[i]] = 0

print(my_dict)
result = []

for k in my_dict:
    result.append(k)
print(result)
