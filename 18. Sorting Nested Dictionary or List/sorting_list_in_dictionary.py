details = {
    "anirudh": [32, 12, 98, 95, 52],
    "vandana": [34, 76, 53, 29, 12],
    "ganesh": [45, 98, 91],
    "hiral": [23, 15, 64, 55],
    "prerna": [56, 49, 87, 64, 29],
}


# print(details.items())
x = dict(sorted(details.items(), key=lambda x: sum(x[1])))
# x = dict(sorted(details.items(), key=lambda x: x[1][-1]))
# x = dict(sorted(details.items(), key=lambda x: max(x[1])))
print(x)
for name, marks in x.items():
    print(f"Name = {name}, marks = {sum(marks)}")
