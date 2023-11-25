# Creating our own error 
# syntax
# raise ExceptionName ("Error message")
# a = int(input("Enter positive number only : "))
# if a > 0:
#     print("Success!!")
# else:
#     # raise Exception("Only Positive Number Allowed")
#     raise ValueError("Only Positive Number Allowed")


# name = input("Enter name of any programming language  : ")
# prgms = ['python', 'java', 'c', 'c++', 'ruby', 'perl', 'swift']
# try:
#     if name in prgms:
#         print("Perfect!!!")
#     else:
#         raise NameError("Invalid programming language")
# except NameError as e:
#     print(e)
# except:
#     print("Some error occured")
    


try:
    print("Hello")
finally:
    print("finally")


# try - finally  => allowed
# try - except   => allowed

# try - else           => Not allowed
# try - finally - else => Not allowed
# only try             => Not allowed