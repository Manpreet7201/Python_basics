
def Calculator():
    print("Welcome to the simple calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("That's not a valid number.")
        return False


    print("Select operation you want to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    try:
        option = int(input("Enter your choice (1/2/3/4):"))
    except ValueError:
        print("Invalid Option")
        return False

    if(option == 1):
        res = num1 + num2
        print(f"The sum of {num1} and {num2}  is: {res}")
    elif(option == 2):
        res = num1 - num2
        print(f"The minus of {num1} and {num2}  is: {res}")
    elif(option == 3):
        res = num1 * num2
        print(f"The multiply of {num1} and {num2}  is: {res}")
    elif(option == 4):
        if(num2 != 0):
            res = num1 / num2
            print(f"The division of {num1} and {num2}  is: {round(res,2)}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("invalid operation you have choosed, please select a valid operation (1/2/3/4).")

while True:
    result = Calculator()
    if result == False:
        continue
    again = input("Do you want to calculate again ?  Yes or No - ")
    if again.lower() in ['yes', 'y'] :
        continue
    else:
        print("Thank you for using the calculator. Goodbye!")
        break