#Set operation
set_A={1,8,7,9,90}
print(set_A)
set_B={2,3,4,5,6,7,8}
# TODO does not allow duplicates
#used for AND \and OR operations
#AND or Union
print(set_A & set_B)
#OR or Intersection
print(set_A | set_B)


print(dir(set_A))

#Assignments

set_A.add(1)
print(set_A)

#pop removes the first element

# remove removes the specific element


print(set_A.difference(set_B))