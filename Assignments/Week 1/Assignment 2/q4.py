number = int(input("Enter a number = "))

# Check the type of number
if number == 0:
    print("Zero")
elif number > 0 and number % 2 == 0:
    print("Positive and Even")
elif number > 0 and number % 2 != 0:
    print("Positive and Odd")
elif number < 0 and number % 2 == 0:
    print("Negative and Even")
else:
    print("Negative and Odd")
