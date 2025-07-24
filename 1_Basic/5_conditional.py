# grading system
marks = int(input("Enter your marks: "))

if marks<=100 and marks>=0:
    if marks>=80:
        print("Grade A+")
    elif marks<80 and marks>=70:
        print("Grade A")
    elif marks<70 and marks>=60:
        print("Grade B")
    elif marks<60 and marks>=50:
        print("Grade C")
    elif marks<50 and marks>=40:
        print("Grade D")
    else:
        print("Fail")
else:
    print("Invalid")