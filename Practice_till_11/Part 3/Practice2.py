# Find common elements between two lists using sets.
lst1 = [90, 12, 56, 8]
lst2 = [2, 46, 18, 90,12]
mySet1 = set(lst1) 
mySet2 = set(lst2)
# comm = mySet1.union(mySet2)
comm = mySet1.intersection(mySet2)
# comm = mySet1.difference(mySet2)
# comm = mySet2.difference(mySet1)
# comm = mySet2.symmetric_difference(mySet1)
print(comm)