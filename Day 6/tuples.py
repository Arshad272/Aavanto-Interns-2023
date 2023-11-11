# tuples - used to store more than one element inside a variable

# they are also heterogeneous - we can store different types of data inside a single tuple 
# they are immutable - which means we cannot modify a tuple after declaring
# they are declared using open braces / paranthesis - ()

# syntax : 
# tuple_name = ( elements, elements ) 
tup = (10,20,630,'hello', 'python')
#      0  1  2    3        4
# print(tup)
# print(type(tup))
# print(tup[2]) 
# print(tup[1:4])
# tup[1] = 500 # error 
# print(tup) 

# print(tup.count(10))
# index() - it will return the index number of an element 
print(tup.index(630))