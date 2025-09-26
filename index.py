name = input("Enter your name: ")
grade_marks = float(input("What is your mark?"'\n'))

if grade_marks < 0 or grade_marks > 100:
    print("Enter a valid mark\u2757")
else:
    print("--**-- RESULT --**--")
    print("Name:", name)
    if grade_marks >= 80:
        print("Your grade is: A+ \U0001F389")
    elif grade_marks >= 70:
        print("Your grade is: A \U0001F64C")
    elif grade_marks >= 60:
        print("Your grade is: B \U0001F44F")
    elif grade_marks >= 50:
        print("Your grade is: C \U0001F44D")
    elif grade_marks >= 40:
        print("Your grade is: D \U0001F44E")
    else:
        print("\U0000274C You didn't get pass marks \U0001F622")