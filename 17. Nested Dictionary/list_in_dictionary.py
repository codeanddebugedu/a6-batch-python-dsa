details = {
    "anirudh": [32, 12, 98, 95, 52],
    "vandana": [34, 76, 53, 29, 12],
    "ganesh": [45, 98, 91],
    "hiral": [23, 15, 64, 55],
    "prerna": [56, 49, 87, 64, 29],
}


for name, marks in details.items():
    total = 0
    for mark in marks:
        total = total + mark
    print(f"Name = {name}, Total = {total}")


# for name, marks in details.items():
#     print(f"Name = {name} | Marks = {sum(marks)}")
