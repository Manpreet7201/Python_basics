# 📌 List Questions:

# Create a list of 5 numbers and print the max and min value.
# my_list  = []
# lent = 5
# i = 0
# while i<5:
#     n1 = int(input("Enter elements- "))
#     my_list.append(n1)
#     i += 1
# print("Maximum- ",max(my_list))
# print("Minimum- ",min(my_list))


# Append an item to a list using append() and insert() at position 2.
# my_list  = ["Hi", 23.00, True, 78]
# my_list.append("last")
# my_list.insert(2,"apple")
# print(my_list)


# Sort a list in ascending and descending order.
# my_list  = [-9, 23, 4, 78]
# my_list.sort()  # ascending order
# print(my_list)
# my_list.sort(reverse=True)  # decending order
# print(my_list)


# Reverse a list without using reverse method (list[::-1]).
# my_list  = [-9, 23, 4, 78,89,0,34]
# reversed_list = []
# for i in range(len(my_list)-1,-1,-1):
#     reversed_list.append(my_list[i])
# print(reversed_list)


# 📌 Tuple Questions:

# Create a tuple and print its type.
# my_tuple = (1,2,3,3)
# print(type(my_tuple))
# print(my_tuple)

# Convert a tuple to a list, modify it, then convert it back.
# my_tuple = (1,2,3,3)
# my_list = list(my_tuple)
# my_list.append("HIIII")
# print(type(my_list))
# print(my_list)
# my_tuple = tuple(my_list)
# print(type(my_tuple))
# print(my_tuple)

# Concatenate two tuples.
# my_tuple1 = (1,2,3,3)
# my_tuple2 = ("Hi","How","Mann")
# my_tuple3 = my_tuple1 + my_tuple2
# print(my_tuple3)

# Count how many times a value appears in a tuple.
# my_tuple = (1,2,3,3,"Hi","Hi",1,"55","89")
# my_dict = dict()
# for i in my_tuple:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# print(my_dict)


# 📌 Dictionary Questions:

# Store student info (name, age, marks) in a dictionary and print it.
# my_dict = {
#     "name": "Manpreet Kaur",
#     "age": 24,
#     "marks": 100
# }
# print(my_dict)

# Update marks of a student.
# my_dict["marks"] = 90
# print(my_dict)

# Add a new key "grade" to the dictionary.
# my_dict["skills"] = "java,python"
# my_dict.update({"hobby": "Dance,drawing"})
# my_dict.update({"skills": "java, python"})
# print(my_dict)

# Print all keys and values separately using keys() and values().
# print(my_dict.keys())
# print(my_dict.values())


# 📌 Set Questions:

# Create two sets and print their intersection, union, and difference.
# s1 = {1,2,3}
# s2 = {4,5,"Hii","Hii",1,2,3}
# s3 = s1.union(s2)
# s3 = s1.intersection(s2)

# s1 = {1, 2, 3}
# s2 = {1, 2, 3, 4, 5} 
# s3 = s1.difference(s2)
# s3 = s2.difference(s1)
# s3 = s1.symmetric_difference(s2)
# print(s3)

# Add a new element to a set.
# s1 = {1, 2, 3}
# s1.add(45)
# print(s1)

# Remove an element using remove() and discard() and note the difference.
# s1 = {1, 2, 3, 45}
# # s1.remove(45)
# s1.discard(4)   # if not present element , then no error will appear
# print(s1)