"""
Anirudh
maths = 23
english = 54
hindi = 98
Vandana
maths = 23
english = 54
hindi = 98
"""

details = {
    "anirudh": {"maths": 23, "english": 54, "hindi": 98},
    "vandana": {"maths": 12, "english": 43, "hindi": 48, "sst": 43},
    "akul": {"maths": 34, "english": 34, "hindi": 85},
    "sanjay": {"maths": 12, "english": 56, "hindi": 83},
    "muskan": {"maths": 54, "english": 76},
}


# How to access
# print(details["sanjay"]["hindi"])


for name, marks in details.items():
    # print(f"Name = {name} | Marks = {marks}")
    print(name)
    for k, v in marks.items():
        print(f"{k} = {v}")
