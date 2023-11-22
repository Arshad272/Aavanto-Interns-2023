# Module - Pre written python code

# 3 types of modules
# 1 - user defined modules 
# Here, we create our own modules. 

# 2 - built in modules
# These modules comes along with the installation of python interpreter

# 3 - third party modules
# We need to install these modules before using

# how to import a module ?
# syntax
# import module_names

# To call the function inside a module
# module_name.function_name() 

# user defined module 
# import calculator 
# calculator.add(10, 5)
# calculator.multiply(10 , 3)


import math 
# sqrt - square root 
# x = math.sqrt(81)
# x = math.sin(90)
# factorial of n is multiplication / product of all numbers from 1 to n
# fact of 5 is = 1 x 2 x 3 x 4 x 5 = 120
# x = math.factorial(6) 
# x = math.pow(5, 3)
# print(x) 

import os 
# mkdir() - make directory - which is used to create a new folder
# os.mkdir("Hello") 
# rmdir() - remove directory - which is used to delete a existing folder 
# os.rmdir("Hello")



l = [1,2,3,4,5]
print(l)
l[0], l[-1] = l[-1], l[0]
print(l) 