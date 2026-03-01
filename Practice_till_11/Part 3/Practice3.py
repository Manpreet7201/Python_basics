# Check if one set is subset of another.lst1 = [90, 12, 56, 8]
lst1 = [90, 12, 56, 8]
lst2 = [2, 46, 18, 90,12, 56, 8]
mySet1 = set(lst1) 
mySet2 = set(lst2)
print(mySet1.issubset(mySet2))
# print(mySet2.issuperset(mySet1))