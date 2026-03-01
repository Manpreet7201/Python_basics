# Reverse a list without slicing.
myLst = [1,2,0,12,8,9,100,3,66,89]
# new_lst = myLst[::-1]
# print(new_lst)

new_lst = []
for i in range(0, len(myLst)):
    new_lst.append(myLst[len(myLst)-1-i])
print(new_lst)