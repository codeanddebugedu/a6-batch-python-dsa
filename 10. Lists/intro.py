# Lists - To store multiple values of different data types [Mutable]
# Array - To store multiple values of same data types

from typing import List

my_list = [2, 6, "Anirudh", True, False, 55.43]
print(my_list)
print(type(my_list))


my_list1 = []
print(my_list1)
print(type(my_list1))


my_list2: list[int] = [5, 5, 7, 4, 1, 4, 7]
print(my_list2)
print(type(my_list2))


my_list3: List[int | str] = [5, 5, 7, 4, 1, 4, 7, "Anirudh"]
print(my_list3)
print(type(my_list3))
