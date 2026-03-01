# Count how many times each element appears in a list.
my_lst = ['NEW ITEM', True, 98.76, 12, 98.76, True]
my_dict = {}
for i in my_lst:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1

print(my_dict)