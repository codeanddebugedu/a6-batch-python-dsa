details = {
    "anirudh": {"maths": 23, "english": 54, "hindi": 98},
    "vandana": {"maths": 12, "english": 43, "hindi": 48, "sst": 43},
    "akul": {"maths": 34, "english": 34, "hindi": 85},
    "sanjay": {"maths": 12, "english": 56, "hindi": 83},
    "muskan": {"maths": 54, "english": 76},
}


# print(details.items())
# x = dict(sorted(details.items(), key=lambda x: x[1]["english"]))
x = dict(sorted(details.items(), key=lambda x: sum(x[1].values())))
print(x)
