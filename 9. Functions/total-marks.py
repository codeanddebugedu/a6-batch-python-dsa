def total_marks(physics, chem, computer, english=0, hindi=0):  # Default/Required
    print(f"You scored {physics} marks in physics")
    print(f"You scored {chem} marks in chem")
    print(f"You scored {computer} marks in computer")
    print(f"You scored {english} marks in english")
    print(f"You scored {hindi} marks in hindi")
    total = physics + chem + computer + english + hindi
    print(f"Your total score is = {total}")


# total_marks(english=55, hindi=33, computer=21, physics=99, chem=43)  # Named Parameters
# total_marks(34, 53, english=43, hindi=11, computer=89)  # Named Parameters
# total_marks(physics=34, 53, english=43, hindi=11, computer=89)  # Named Parameters (Error)
total_marks(computer=44, physics=55, chem=66)
