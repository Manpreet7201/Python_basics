# Store student marks of 5 subjects and print average.
myInp = int(input("Enter the number of subjects you want to count avg of them - "))
my_dict = {}
for i in range(0, myInp):
    subject = input("Enter Subject name- ")
    marks = int(input("Enter Subject marks- "))
    my_dict[subject] = marks

print(my_dict)

def avrg(my_dict):
    total = 0
    for mark in my_dict.values():
        total += mark
    return total/len(my_dict)

print("Average - ", avrg(my_dict))