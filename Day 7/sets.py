# sets
# they are declared or created using curly braces - {}
# They are also used to store multiple elements. 
# In Python, we can create a set by passing comma-separated values inside the curly braces. 

# Elements inside a set are stored in random memory location (they are not in contiguous order)
# Hence, it is not possible to perform indexing and slicing in sets 

# sets does not allow ducplicate elements. it consists only unique elements. 

# a = {1,2,3,6,5, 1 , 2 , 1 , 1 , 2} 
# print(a) 
# print(len(a)) 
# print(type(a)) 
# print(a[0]) # error 

a = {1,2,3,4,5}
b = {4,5,6,7,8}
# union
# it will combine elements of both sets. it will ignore duplicate elements. 
# c = a.union(b)

# intersection
# it will return common elements from both sets 
# c = a.intersection(b)

# difference 
# it will return all elements from set 'a' which are not in set 'b' 
# c = a.difference(b) 
# print(c) 

# a.clear()

# a.add(10)

# pop() - it will delete a random element from a set 
# print(a.pop()) 
# print(a) 

a = {1,2,3,4,5,6}
b = {2,4,5}

# subset 
#  if all the elements of B is present in A, then B is subset of A
# print(b.issubset(a)) 
# print(a.issubset(b)) 

# superset 
# if all the elements of A is present in B, then A is super set of B
# print(a.issuperset(b)) 
# print(b.issuperset(a)) 