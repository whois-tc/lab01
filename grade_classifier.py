raw_grade= input("Enter your grade") #Input a range between 0 and 100
try:
    grade = float(raw_grade)
except ValueError:
    print("Invalid input. Enter a number from 0 to 100")
    raise SystemExit(1)
if not 0 <=grade <=100:
    print(f"{grade} is outside the valid range of 0 to 100.")
    raise SystemExit(1)
if grade >= 80:
    letter_grade = "A"
elif grade >= 70:
    letter_grade = "B"
elif grade >= 60:
    letter_grade = "C"
elif grade >=50:
    letter_grade = "D"
else:
    letter_grade = "F"
print(f"Your grade of {grade} is classified as {letter_grade}.")
