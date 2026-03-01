# Find the longest word in a sentence.
user = input("Please enter an sentence.")
lst = user.split()
print(lst)
maxLen = ''
for i in lst:
    if len(i) > len(maxLen):
        maxLen = i

print(maxLen)