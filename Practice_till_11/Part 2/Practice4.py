# Convert a tuple to list, modify it, convert back.

my_tuple = (12,"hi", 98.76, True)
print(my_tuple)
my_lst = list(my_tuple)
my_lst.append("NEW ITEM")
my_lst.reverse()
my_lst.pop(3)
print(my_lst)
my_tuple_new = tuple(my_lst)
print(my_tuple_new)
