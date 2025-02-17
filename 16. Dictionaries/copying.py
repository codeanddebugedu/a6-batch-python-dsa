# Mutable

d1 = {
    "Physics": 56,
    "Chemistry": 12,
    "English": 99,
    "Computer": 22,
    "Maths": 94,
}


d2 = d1.copy()
d2["Maths"] = 100


print(d1)
print(d2)
