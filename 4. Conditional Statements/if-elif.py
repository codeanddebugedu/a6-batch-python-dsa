age = int(input("Enter your age = "))

if age >= 18:
    print("Adult")
if age >= 13 and age <= 17:
    print("Teen")
if age >= 0 and age <= 12:
    print("Child")
else:
    print("Invalid")
