class Person:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")

    def display_person_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll_no = int(input("Enter student roll number = "))
        self.physics = int(input("Enter marks of physics = "))
        self.chemistry = int(input("Enter marks of chemistry = "))

    def display_student_details(self):
        print(f"Student name = {self.name}")
        print(f"Student age = {self.age}")
        print(f"Student gender = {self.gender}")
        print(f"Student roll_no = {self.roll_no}")
        print(f"Student physics = {self.physics}")
        print(f"Student chemistry = {self.chemistry}")


p1 = Student()
p1.display_student_details()
