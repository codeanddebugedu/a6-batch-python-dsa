math_score = int(input("Enter your Math score = "))
science_score = int(input("Enter your Science score = "))
english_score = int(input("Enter your English score = "))

total_score = math_score + science_score + english_score

if (
    math_score >= 70
    and science_score >= 65
    and english_score >= 60
    and total_score >= 200
):
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
