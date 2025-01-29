weight = float(input("Enter your weight in kg = "))
height = float(input("Enter your height in meters = "))

# Calculate BMI
bmi = weight / (height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are Underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}. You have a Normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}. You are Overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You have Obesity.")
