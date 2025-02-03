"""
Keep on asking a integer from user. Until he enters 0

Enter a number = 3
Enter a number = 1
Enter a number = 10
Enter a number = 5
Enter a number = 0

Total = 19
Average = Total/total numbers = 19/4 = 4.85
"""

total = 0
count = 0
while True:
    num = int(input("Enter a number = "))
    if num == 0:
        break
    total = total + num
    count += 1

print(f"Total = {total}")
avg = total / count
print(f"Average = {total}")
