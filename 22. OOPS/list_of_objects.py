from typing import List


class Student:
    def __init__(self):
        self.roll_no: int = int(input("Enter a roll number = "))
        self.name: str = input("Enter name = ")
        self.gender: str = input("Enter gender = ")
        self.marks: List[int] = []
        for _ in range(4):
            m = int(input("Enter marks = "))
            self.marks.append(m)

    def displayMarks(self):
        for i in range(4):
            print(f"Marks = {self.marks[i]}")
        print(f"Total marks scored = {sum(self.marks)}")

    def updateMarks(self):
        self.marks.clear()
        for _ in range(4):
            m = int(input("Enter marks = "))
            self.marks.append(m)

        # Alternate way 👇
        # for i in range(4):
        #     m = int(input("Enter marks = "))
        #     self.marks[i] = m

    def display(self):
        print(f"\nStudent roll no = {self.roll_no}")
        print(f"Student name = {self.name}")
        print(f"Student gender = {self.gender}")
        print(f"Student marks = {self.marks}")

    def update(self):
        self.name = input("Enter new name = ")


all_students: List[Student] = []

while True:
    print("\n1. Add a student")
    print("2. View all students")
    print("3. Update student details")
    print("4. Display marks of a particular student")
    print("5. Update marks of a particular student")
    print("6. Exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Student()
        all_students.append(obj)
        # print(all_students)
    elif choice == 2:
        if len(all_students) == 0:
            print("No student has been added yet")
        else:
            for st in all_students:
                st.display()
    elif choice == 3:
        roll_number = int(input("Enter student roll number you want to update = "))
        for st in all_students:
            if st.roll_no == roll_number:
                st.update()
                break
    elif choice == 4:
        roll_number = int(
            input("Enter student roll number you want to check marks of = ")
        )
        for st in all_students:
            if st.roll_no == roll_number:
                st.displayMarks()
                break
    elif choice == 5:
        roll_number = int(
            input("Enter student roll number you want to udpate marks of = ")
        )
        for st in all_students:
            if st.roll_no == roll_number:
                st.updateMarks()
                break
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
