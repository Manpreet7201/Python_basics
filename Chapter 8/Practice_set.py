# Problem 1  - find greater number
# def myFunc(a,b,c):
#     if a>b and a>c :
#         greater = a
#     elif b>a and b>c:
#         greater = b
#     else:
#         greater = c
    
#     return greater
# a = int(input("Enter 1 number- "))
# b = int(input("Enter 2 number- "))
# c = int(input("Enter 3 number- "))
# ans = myFunc(a,b,c)
# print(ans)


# Problem 2  - function convert temp cel to fehrenheit
# F = C * 1.8 + 32     # 1.8 = 9/5
# def myFunc(temp):
#     val =  temp*1.8+32   
#     return val
# Cel = int(input("Enter temp in celsius- "))
# ans = myFunc(Cel)
# print(ans)


# Problem 3  - function to prevent new line using print function
# print("a")
# print("b")
# print("c", end="")
# print("d", end="")
# print("e")


# Problem 4  - function to print 1st n natural numbers
# sum(1) = 1
# sum(2) = 1+2
# sum(3) = 1+2+3
# sum(4) = 1+2+3+4
# sum(n) = 1+2+3+4+......+(n-1)+n
# or sum(n) = sum(n-1) + n
# def cal(n):
#     if n==1:
#         return 1 
#     return cal(n-1)+n
# a = int(input("Enter number- "))
# print(cal(a))


# Problem 5  - function to print pattern
# def pattern(n):
#     if n==0:
#         return
#     print("*"*n)
#     pattern(n-1)

# a = int(input("Enter number- "))
# # print(pattern(a))
# pattern(a)


# Problem 6  - function to convert inches to cms
#  cms = inches * 2.54
# def myFunc(inches):
#     cms = inches * 2.54  
#     return cms
# inches = int(input("Enter value in inches- "))
# ans = myFunc(inches)
# print(ans)


# Problem 7  - function to remove a given word from a list and strip it at the same time
def findWord(word, myList):
    word = word.strip()
    new = []
    for item in myList:
        item = item.strip()
        if item != word:
            new.append(item)
    return new
myList = ["Hii", " an ", " jannu"]
print(findWord(" Hii  ", myList))



# Problem 8  - function to type a table of multiplication
# def multi(num, i=1):
#     if i>10:
#         return 
#     print(f"{num} * {i} = {num*i}")
#     multi(num,i+1)

# num = int(input("Enter the number- "))
# multi(num)