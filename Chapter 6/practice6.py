marks = int(input("Enter your marks to find out your grade- "))

if (marks<=100 and marks>=90):
    print("Grade: Excellent")
elif (marks<90 and marks>=80):
    print("Grade: A")
elif (marks<80 and marks>=70):
    print("Grade: B")
elif (marks<70 and marks>=60):
    print("Grade: C")
elif (marks<60 and marks>=50):
    print("Grade: D")
elif(marks<50):
    print("Grade: F")