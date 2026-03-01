marks1 = int(input("Enter marks for 1st subject:- "))
marks2 = int(input("Enter marks for 2nd subject:- "))
marks3 = int(input("Enter marks for 3rd subject:- "))

total_per = ((marks1+marks2+marks3)*100)/300
# at_least1 = (marks1*33)/100
# at_least2 = (marks2*33)/100
# at_least3 = (marks3*33)/100

if(total_per >=40 and marks1>=33 and marks2>=33 and marks2>=33):
    print("Passed with percentange- ", total_per, "%")
else:
    print("Failed with percentange- ", total_per, "%")