# Dictionaries 
# They are key and value pairs
# Key is unique, but values can be repeated.
# they are also created using curly braces - {}

# key and value should be separated using COLEN :
# key value pairs should be separated using comma , 
# syntax 
# dict = {key : value, key : value}

d = {1 : 'one', 2 : 'two', 3 : 'three', 1: 'hello'}
# print(d) 
# print(type(d)) 
# print(len(d)) 

# to access values - dict[key]
# print(d[1]) 

d = {'a': 'hello 1', 'b': 'hello 2', 'c': 'hello 3'}
# print(d['b'])  

# keys() - it will return all keys in a dictionary
# print(d.keys()) 

# values() - it will return all the values of dictionary
# print(d.values()) 

# to add new key and value pair
# dict[key] = new_value
# d['d'] = 'hello 4'
# print(d) 