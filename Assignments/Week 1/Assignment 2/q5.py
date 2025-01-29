marks1 = int(input("Enter marks in Subject 1 = "))
marks2 = int(input("Enter marks in Subject 2 = "))
marks3 = int(input("Enter marks in Subject 3 = "))

# Average marks
average_marks = (marks1 + marks2 + marks3) / 3

if average_marks > 90:
    print("Grade A")
elif 80 < average_marks <= 90:
    print("Grade B")
elif 70 < average_marks <= 80:
    print("Grade C")
elif 60 < average_marks <= 70:
    print("Grade D")
else:
    print("Fail")
