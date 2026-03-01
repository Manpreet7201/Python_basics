#  Recursion means a function calling itself to solve a problem.
# Base Case → when recursion stops
# Recursive Call → function calls itself

# def myFunc(n):
#     # base case
#     if n == 0:
#         return
#     # recursive call
#     myFunc(n-1)
#     print(n)

# myFunc(10)

def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)

# a = fact(3)
# print(a)
val = int(input("Enter any number- "))
print(f"The factorial of {val} is = {fact(val)}")