# try - except - else
# If there is no error in TRY block means, then the code present inside ELSE block will get executed
# try:
#     code
# except:
#     code
# else:
#     code

# try:
#     print("Hello")
#     a = 10
#     b = 20
#     print(a)
#     print(a + b)
# except:
#     print("Error occured!!!!")
# else:
#     print("No Error Occured")




# try - except - else - finally
# The code present inside FINALLY block will always get exceuted
# try:
#     code
# except:
#     code
# else:
#     code
# finally:
#     code

try:
    print("Hello")
    a = 10
    print(10 / 0)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except:
    print("Some other error")
else:
    print("No Error Occured")
finally:
    print("Program Ended!!!!")

# ERROR - except and finally
# NO ERROR - else and finally