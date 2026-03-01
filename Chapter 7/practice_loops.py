# prob 1
# multiplication tabel
# table = int(input("Enter number for which table you want:- "))
# for i in range(1,11):
#     print(str(table) + " * "+ str(i) +" = "+ str(table*i))
#     print(f"{table} * {i} = {table*i}")


# prob 2
# l = ["Harry", "Sohan", "Sachin", "Rahul","Sneha"]

# for i in l:
#     if i.startswith("S"):
#         print("Hi , good morning," + i)


# prob 3
# table = int(input("Enter number for which table you want:- "))
# i = 1
# while i<=10:
#     print(str(table) + " * "+ str(i) +" = "+ str(table*i))
#     i += 1


# prob 4
# num = int(input("Emter the number:- "))
# for i in range(2,num):
#     if num%i==0:
#         print("Number is not prime")
#         break  # if divide by 2 then np need to go further becoz already it is not prime num now
    
# else:
#     print(f"{num } Number is prime")


# prob 5 - sum of first n natural numbers
# n = int(input("Emter the number:- "))
# i  = 1
# s = 0
# while (i<=n):
#     s = s+i 
#     i+=1
# print(s)


# prob 6 - factorial of a number
# n = int(input("Emter the number:- "))
# fact = 1
# for i in range(1,n+1):
#     fact = i * fact
# print(f"Factorial of {n} is: {fact}")


# prob 7 - print like this
'''
n = 3
  *
 ***
*****

'''
# n = int(input("Emter the number:- "))  #n=3
# for i in range(1, n+1):
#     print(" " *(n-i), end="")
#     print("*"*(2*i-1))
#     print( )


# prob 8 - print like this
'''
n = 3
*
**
***

'''
# n = int(input("Emter the number:- "))  #n=3
# for i in range(1, n+1):
#     print("*"*(i), end="")
#     print(" " *(n-i))
#     print( )


# prob 9 - print like this
'''
n = 3
***
* *
***

'''
# n = int(input("Emter the number:- "))  #n=3
# for i in range(1, n+1):
#     if i==1 or i==n:
#         print("*"*(n), end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2),end="")
#         print("*", end="")
#     print( )


# prob 10 - multiplication table in reversed order
n = int(input("Emter the number:- "))
for i in range(1,11):
    # print(str(n) + " * "+ str(i) +" = "+ str(n*i))
    print(f"{n} * {11-i} = {n*(11-i)}")
