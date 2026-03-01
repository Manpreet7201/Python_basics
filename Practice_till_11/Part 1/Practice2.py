# Check if a string is a palindrome.
# exm - ABCDCBA

user = input("Please enter an sentence.")
# if user.lower() == user[::-1].lower():
#     print("Palindrome.")
# else:
#     print("Not a Palindrome.")



left = 0
right = len(user)-1
flag = True
while left<right:
    if user[left].lower() != user[right].lower():
        flag = False
        break
    else:
        left += 1
        right -= 1

if(flag == True):
    print("Palindrome.")
else:
    print("Not a Palindrome.")
    

