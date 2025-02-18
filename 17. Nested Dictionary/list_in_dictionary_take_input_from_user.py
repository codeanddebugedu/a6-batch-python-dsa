"""
Enter student name = Anirudh
Enter marks = 
Enter marks = 
Enter marks = 
Enter student name = Vandana
Enter marks = 
Enter marks = 
Enter marks = 
{
    "Anirudh": [32,45,33],
    "Vandana": [58,74,14],
}
"""

details = {}

for _ in range(0, 2):
    name = input("Enter student name = ")
    marks = []
    for _ in range(0, 3):
        m = int(input("Enter marks = "))
        marks.append(m)
    details[name] = marks

print(details)
