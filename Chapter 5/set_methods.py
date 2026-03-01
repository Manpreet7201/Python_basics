s1 = set([1,2,3,"Hii"])
# 
# add() - one item only
# print(s1.add(8))
# print(s1)

# remove()
# s1.remove(1)
# print(s1)

# update() - multiple item only
# print(s1.update([8,"JIII"]))
# # s1.update([( "12", 34, 6.09 )])
# s1.update([34, ( "12", 34, 6.09 )])  # cant add list as set item , because they r mutable, can convert them to tuple
# print(s1)

# claer() and pop()
# s1 = set([1,2,3,"Hii"])
# s2 = {67,34,"Kal"}
# s1 = s.pop()
# s1 = s.clear()
# print(s1)

# union() - combines sets
# s1 = set([1,2,3,"Hii"])
# s2 = {67,34,"Kal","Hii","Jija","oo",3,2}
# s3 = s1.union(s2)
# print(s3)
# s4 = s1.intersection(s2)
# print(s4)
# s5 = s1.difference(s2)
# s6 = s2.difference(s1)
# print(s5)
# print(s6)

# s7 = s1.symmetric_difference(s2)
# print(s7)