# Remove all duplicate characters from a string.
user = input("Please enter an sentence.")
dict_ = {}
newStr = ''
for i in user: 
    if i not in dict_:
        newStr += i
        dict_[i] = True

print(newStr)
print(dict_)
    
