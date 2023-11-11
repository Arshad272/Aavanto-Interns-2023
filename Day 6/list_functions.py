# More about slicing in lists 

lst = [10,20,30,40,50,60,70,80,90]
#      0  1  2  3  4  5  6  7  8
# by default the starting index number is 0 and ending index number is len(lst) - 1
# print(lst[:])
# print(lst[2:])
# print(lst[:6])

lst = [10,20,30,40,50,60,70,80,90]
#      0  1  2  3  4  5  6  7  8
# list_name[ start : end : incr/decr ]
# print(lst[1:8:3])
# 20, 50, 80 

# print(lst[::-1]) 
# 90, 80, 70, 60 , ...


# LISTS ARE MUTABLE - WHICH MEANS WE CAN MODIFY THE ELEMENTS OF A LIST 

lst = [10,20,30,40,50,60,70,80,90]
# pop() - it will delete and return the last element of a list
# print(lst.pop())
# print(lst) 
# lst[1] = 255
# print(lst) 
# list_name.function_name()
# remove() - used to delete an element from a list 
# print(lst.remove(40)) 
# print(lst) 
# clear() - it will delete all elements of list 
# lst.clear()  
# append() - it will add an element at the end of the list 
# lst.append(100)
# extend() - it is used to add more than one element to our list 
# lst.extend([100,110,120,130])
# lst.extend(["hello"]) 
# lst.extend("hello")  

# insert() - it is used to insert an element at specific index position
# insert( index_num, element )
# lst.insert( 1 , 15 )

# count() - it will return the count of element
# print(lst.count(10))

# reverse() - it will reverse all elements of list
# lst.reverse()
# print(lst) 

# sort() -  it will sort all elements in ascending order 
l = [56,23,78,56,2,1,65,7]
# l.sort()
# print(l)

# copy() - used to copy elements from one list to another list 
# a2 = l.copy()
# print(a2) 