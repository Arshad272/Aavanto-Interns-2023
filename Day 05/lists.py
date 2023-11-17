# LISTS
# They are used to store collection of elements
# Lists can contain different data types such as int, float, string etc. - heterogeneous 
# Lists are declared using square braces - []

# Creating a list
# list_name = [element1, element2, element3]
elems = [10,20,30,50,'hello', 10.35, True]
#        0  1  2  3   4        5      6
#        -7 -6 -5 -4  -3      -2     -1
# print(elems[0:-3])
# print(elems[0:5])
print(elems[:])
# Indexing 
# Each and every element in a list will have a index number
# Index numbers starts from 0, and then it will be incremented
# syntax = list_name[index_num]
# print( elems[4] )

# syntax = list_name[index_num] = new_value
# elems[0] = 500
# print(elems)

# negative indexing
# it starts from end of list and it starts from -1

lst = [10,20,30,50,70,80,90]
#      0  1  2  3  4  5  6
# print(lst[-1])
# Slicing
# Used to access more than one element from a list
# syntax - list_name[first_index_num : last_index_num + 1]
# print(lst[2 : 6]) 

# nested lists - list inside another list 
nestedList = [[1,2], [3,4], [5,6], 10, 'hello', 3.14]
# print(nestedList[0][1])


# len() - it will return the total count of elements inside a list 
# print(len(elems)) 