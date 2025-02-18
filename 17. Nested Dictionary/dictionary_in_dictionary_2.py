"""
anirudh has scored 323 marks
vandana has scored 412 marks
"""

details = {
    "anirudh": {"maths": 23, "english": 54, "hindi": 98},
    "vandana": {"maths": 12, "english": 43, "hindi": 48, "sst": 43},
    "akul": {"maths": 34, "english": 34, "hindi": 85},
    "sanjay": {"maths": 12, "english": 56, "hindi": 83},
    "muskan": {"maths": 54, "english": 76},
}
for name, marks in details.items():
    total = 0
    for k, v in marks.items():
        total += v
    print(f"{name} has scored {total} marks")
