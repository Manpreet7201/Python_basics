# 🔹 LEVEL 3 — Loops & Logic Building
# Print numbers from 1–10 using a loop.
# i = 1
# while i<=10:
#     print(f"Number {i}")
#     i+=1

# Print only even numbers from 1–20.
# i = 1
# while i <= 20:
#     if i%2==0:
#         print(f"Even Number- {i}")
#     i+=1

# Print multiplication table of a number entered by the user.
# num = int(input("Enter Number:- "))
# i = 1
# while i<=10:
#     print(f"{num} * {i} = {num*i}")
#     i += 1

# Print sum of all numbers from 1–100.
# sum = 0
# i = 0
# while i<=100:
#     sum += i
#     i += 1
# print(sum)
# s = (100(100+1))/2   # 5050  - sum of 1st n natural numbers formula

# Count vowels in a user-entered string.
# word = input("Enter the string- ")
# i = 0
# count = 0
# vowels = ['a','e', 'i', 'o', 'u']
# while i<len(word):
#     if word[i] in vowels:
#         count += 1
#     i += 1
# print(count) 

# Check if a number is prime.
# num = int(input("Enter Number:- "))
# for i in range(2,num):
#     if num%i == 0:
#         print("Number is not prime.")
#         break
# else:
#     print("Number is prime.")


# Reverse a number using a loop.
# word = input("Enter the string- ")
# new = ""
# for i in range(len(word)-1,-1,-1):
#     new += word[i]
# print(new)


# Print Fibonacci series up to n terms.
# n = int(input("Enter the number- "))
# fibb = []
# a = 0
# b = 1
# for i in range(0, n):
#     fibb.append(a)
#     next = a + b
#     a = b
#     b = next
# print(fibb)

# Find the factorial of a number using a loop.
# num = int(input("Enter the number- "))
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)