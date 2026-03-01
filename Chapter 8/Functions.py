# # function definition
# def myName():
#     name = input("Enter Your name:- ")
#     print("Hi, Good evening Mam!" , name, " A Very good day mam. Thanks for visiting the Taj Hotel." )

# # function call
# myName()


# # function with arguments
# # function definition
# def myName(name):   # works as paramter or formal paramters
#     # name = input("Enter Your name:- ")
#     print("Hi, Good evening Mam!" , name, " A Very good day mam. Thanks for visiting the Taj Hotel." )

# # function call
# myName("Kirat")  # works as argument   or actual paramters

# a function can also return a values
def ReturnFunc(name):  
    ans = "Your name is- " + name
    return ans

ReturnFunc("Kirat") 



# a function with default parameters
def myName(name, ending="Thanks"):
    print("Hi, Good evening," , name, " !" )
    print(ending)

myName("Manpreet", "Thank You")
myName("Mann")

