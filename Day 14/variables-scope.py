# Global variables
# They are declared outside the function
# They can be accessed throughout the program

# Local Variables 
# They are declared inside function
# They can be accessed only inside the function


# def my_function():
#     a = 20
#     print(a)  
# my_function() 
# print(a) 

# a = 10
# def hello():
#     a = 20
#     print(a)
# hello()
# print(a)

# To change the value of global variable inside a function
# global variable_name

# a = 10
# def hii():
#     global a 
#     a = 20
#     print(a)
# print(a)
# hii()
# print(a)


# error - local variable 'b' referenced before assignment
b = 10
def hello2():
    print(b)
    b = 50
    print(b) 
hello2()