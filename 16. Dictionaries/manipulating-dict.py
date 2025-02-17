my_dict = {
    "Physics": 56,
    "Chemistry": 12,
    "English": 99,
    "Computer": 22,
    "Maths": 94,
}
print(my_dict)

# Add/Update
# my_dict.update({"SST": 45})
# my_dict.update({"Physics": 45, "hajkdhwa": 998})
# my_dict["Computer"] = 91
# my_dict["XYZXYZ"] = 100

# Delete
# del my_dict["Chemistry"]
x = my_dict.pop("Chemistry")
# print(x)
print(my_dict)

my_dict.clear()
print(my_dict)
