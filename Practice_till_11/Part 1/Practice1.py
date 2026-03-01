# Take a sentence from user and:
# count vowels
# count consonants
# count spaces

user = input("Please enter an sentence.")
print()
c_v = 0
c_c = 0
c_s = 0
for i in user:
    if i.lower() in ('a','e','i','o','u'):
        c_v += 1
    elif i == ' ':
        c_s += 1
    elif i.isalpha() and i.lower() not in ('a','e','i','o','u'):
        c_c += 1
print(f"Vowels count: {c_v}")
print(f"Constants count: {c_c}")
print(f"Spaces count: {c_s}")