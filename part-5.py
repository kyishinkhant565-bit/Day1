marks = float(input("Enter your marks:"))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else :
    print("Fail")
