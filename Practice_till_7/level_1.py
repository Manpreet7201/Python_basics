# Take a user’s name and print a greeting message.
# username = str(input("Please enter your name:- "))
# print("Hi", username, ", Good morning and Welcome to the class.")

# Take two numbers and print their sum, difference, multiplication and division.
# a = int(input("Enter number 1st- "))
# b = int(input("Enter number 2nd- "))
# print("The sum of the entered numbers is- ", a+b)
# print("The multiplication of the entered numbers is- ", a*b)
# print("The subtract of the entered numbers is- ", a-b)
# print("The division of the entered numbers is- ", a/b)

# Check if a word contains the letter "a".
# word = str(input("Please enter the word:- "))
# lst = word.split(',')
# for i in word:
#     # print(i)
#     if i == 'a':
#         print("Word contains the letter 'a'.")
#         break
# else:
#     print("Word does not contains the letter 'a'.")

# word = input("Please enter the word:- ")

# if 'a' in word:
#     print("Word contains the letter 'a'.")
# else:
#     print("Word does not contain the letter 'a'.")

# print(lst)



# Convert a string to uppercase and lowercase.
# word = input("Please enter the word:- ")
# print("Uppercase: ", word.upper())
# print("Lowercase: ", word.lower()," , " , word.capitalize())

# Count how many times a letter appears in a sentence.
# word = input("Please enter the sentence:- ")
# my_dict = dict()
# for i in word:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# print(my_dict)

# Replace all spaces with _ in a sentence.
# word = input("Please enter the sentence:- ")
# word_replaced = ""
# for i in word:
#     if i == ' ':
#         word_replaced = word.replace(" ", "_")
# print(word_replaced)


# Print the length of a given string.
# word = str(input('Enter the string:- '))
# print("Length of the given word is:- ", len(word))


# Write a program to concatenate two strings using:
word = str(input('Enter the 1 string:- '))
word1 = str(input('Enter the 2 string:- '))
# + operator
# print("Concatenated: ", word+word1)
# f-string
# print(f"Concatenated: {word}{word1}")
# format()
print("Concatenated: {}{}".format(word, word1))