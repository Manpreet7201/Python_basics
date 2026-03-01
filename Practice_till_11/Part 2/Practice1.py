# Take 10 numbers in a list and:
# print even numbers
# print odd numbers
# find second largest number

myLst = [1,2,0,12,8,9,100,3,66,89]

# even and odd numbers function
def EvenFind(lst):
    evn_lst = []
    odd_lst = []
    for i in lst:
        if (i%2==0):
            evn_lst.append(i)
        else:
            odd_lst.append(i)
    print("Even numbers list - ",evn_lst)
    print("Odd numbers list - ",odd_lst)

EvenFind(myLst)


def secondLargest(lst):
    max_ = 0
    sec = 0
    for i in lst:
        if i > max_:
            sec = max_
            max_ = i
        elif(i<max_ and i>sec) :
            sec = i
    print(sec)

secondLargest(myLst)