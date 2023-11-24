
# Error 
# It causes abnormal termination of program
# - 3 categories of errors
# 1. Syntax Error 
# It causes due to invalid syntax. Syntax is set of rules which we should follow. If we don't follow those rules we will get syntax error 

# if 10 > 5
#     print("Hello")

# 2. Logical Errors
# These errors occurs due to invalid logic 
# Here program will not terminate abnoramally. Also in logical errors ERROR messages will not come. 
# Incase of Logical errors, user will not get the valid output. 

# def add(a, b):
#     print(a * b)
# add(10 , 20)

# 3. Run time errors  
# These run time errors occurs during the execution of a program 

# print("Hello")
# print(a)
# print("Hello 2")

# if 10 > 5
#     print("Hello")

# Exception handling - preventing errors 

# First interpreter will execute the code present inside TRY block
# If any error occurs means, then the code present inside EXCEPT block will get executed 
# In case of ZERO errors, EXCEPT block will not get executed

# try: 
#     code
#     code
#     code
# except ExceptionName:
#     code
#     code
#     code


# try:
#     print("Hello")
#     print(a)
# except:
#     print("Error occured")


# try:
#     print("Hello")
#     d = {1 : 'one'}
#     print(d[2])

# except NameError:
#     print("Invalid Variable Name")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except IndexError:
#     print("Invalid index number")

# except:
#     print("Some other error")


# try:
#     if 1 > 0 
#         print("Hii")

# except:
#     print("Error occured")