# Replace every space with _ without using replace().

user = input("Please enter an sentence.")
new = ''
for i in user:
    if i == ' ':
        new += "_" 
    else:
        new += i
    
print(new)