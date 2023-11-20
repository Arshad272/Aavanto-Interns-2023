# It is a block of code used to do a specific job / task 
# The code present inside function will be executed only when we call it 
# We can create a function once and we can call it multiple times 

# syntax 
# def function_name( arguments, arguments ):
#     code
#     code
# code

# call a function 
# function_name( parameters )

# Types
# 1 - function without parameters and function without return
# 2 - function with parameters and function without return
# 3 - function without parameters and function with return
# 4 - function with parameters and function with return


# 1st

def sayHello():
    print("Hello")

# x = sayHello() 
# print(x)
# sayHello() 
# sayHello() 
# sayHello() 



# 2nd 

def add(a, b):
    print(a + b) 

# add(10, 20)

# 3rd 
def sayHii():
    return "Hii"

# print(sayHii())
# x = sayHii()
# print(x) 

# 4th 

def multiply(a, b):
    c = a * b 
    return c 

# x = multiply(5, 2) 
# print(x) 

x = "Python"
l = len(x) 
print(l) 