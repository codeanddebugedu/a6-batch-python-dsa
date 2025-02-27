class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, roll_no, physics, chemistry):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
        self.physics = physics
        self.chemistry = chemistry

    def display_student_details(self):
        print(f"Student name = {self.name}")
        print(f"Student age = {self.age}")
        print(f"Student gender = {self.gender}")
        print(f"Student roll_no = {self.roll_no}")
        print(f"Student physics = {self.physics}")
        print(f"Student chemistry = {self.chemistry}")


p1 = Student("Anirudh", 11, "Male", 3, 56, 89)
p1.display_student_details()
