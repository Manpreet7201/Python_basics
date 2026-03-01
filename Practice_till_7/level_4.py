# 🔹 LEVEL 4 — Pattern Printing (Logic Boost)
'''
    ****
    ****
    ****
    ****
'''
# n = int(input("Enter the number:- "))  #n=3
# i = 0
# for i in range(0,n):
#     j = 0
#     for j in range(0,n):
#         print("*", end="")
#     print()
# n = int(input("Enter the number: "))
# for i in range(n):
#     print("*" * n)
# i = 0
# while i<n:
#     j = 0
#     while j<n:
#         print("*", end=" ")
#         j = j + 1
#     print()
#     i = i+1


'''
    *
    **
    ***
    ****
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 0
#     while j<i+1:
#         print("*", end="")
#         j+=1
#     print()
#     i+=1


'''   
    *
   ***
  *****
 *******
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 0
#     while j<((n-i)-1):
#         print(" ", end="")
#         j+=1

    # j = 0
    # while j<(2*i+1):
    #     print("*", end="")
    #     j+=1
    # print()
    # i+=1

'''
    *****
    *   *
    *   *
    *****
'''
# r = int(input("Enter the number of rows:- "))
# c = int(input("Enter the number of columns:- "))
# for i in range(0,r):
#     if i==0 or i==r-1:
#         print("*"*c)
#     else:
#         print("*" + " "*(c-2) + "*")

# r = int(input("Enter the number of rows:- "))
# c = int(input("Enter the number of columns:- "))
# i = 0
# while i<r:
#     if i==0 or i==r-1:
#         print("*"*c)
#     else:
#         print("*" + " "*(c-2) + "*")

#     i = i+1

'''
***
**
*
'''
# n = int(input("Enter the number of rows:- "))
# i = 0
# while i<n:
#     j = 0
#     while j<n-i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1

'''
  *
 **
***
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 0
#     while j<((n-i)-1):
#         print(" ", end="")
#         j+=1
#     j = 0
#     while j<(i+1):
#         print("*", end="")
#         j+=1

#     print()
#     i+=1


'''
*****
 ***
  *
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 0
#     while j<i:
#         print(" ", end="")
#         j+=1
#     j = 0
#     while j<(2*(n-i)-1):
#         print("*", end="")
#         j+=1

#     print()
#     i+=1


'''
1
12
123
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 1
#     while j<=i+1:
#         print(j, end="")
#         j+=1
#     print()
#     i+=1

'''
1
22
333
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 1
#     while j<=i+1:
#         print(i+1, end="")
#         j+=1
#     print()
#     i+=1

'''
123
12
1
'''
# n = int(input("Enter the number:- "))
# i = 0
# while i<n:
#     j = 1
#     while j<=n-i:
#         print(j, end="")
#         j+=1
#     print()
#     i+=1


'''
1
2 3
4 5 6
'''
# n = int(input("Enter the number:- "))
# i = 0 
# num = 1
# while i<n:
#     j = 1
#     while j<=i+1:
#         print(num, end="")
#         j+=1
#         num+=1
#     print()
#     i+=1
    # num+=1

# pending this question ############################################
'''
  *
 * *
*****
'''
# n = int(input("Enter the number:- "))
# for i in range(0,n):
#     for j in range(1,2*n):
#         if j == 0 or i == n-1 or 




'''
  *
 * *
*   *
 * *
  *
'''