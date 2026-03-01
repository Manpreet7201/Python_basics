# Prob 1
a = int(input("Enter 1st number- "))
b = int(input("Enter 2nd number- "))
c = int(input("Enter 3rd number- "))
d = int(input("Enter 4th number- "))

if(a>b and a > c and a>d):
    print("a is greater than b,c and d")
elif(b>a and b>c and b>d):
    print("b is greater than a,c and d")
elif(c>b and c>a and c>d):
    print("c is greater than a,b and d")
else:
    print("d is greater than b,c and a")