# Count frequency of each character in a string (dict).
myStr = input("Enter any string to count charaters count - ")
my_dict = {}
for i in myStr:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

print(my_dict)