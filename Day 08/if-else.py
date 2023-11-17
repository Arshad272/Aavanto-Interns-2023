# Conditional Statements 
# Depending upon condition, if we want to run specific block of code means, we can use conditional statements 

# syntax 
# if condtion :
#     code 

# example 
# if 10 < 5 : 
#     print("Hello")
#     print("hello 2")
#     print("byee")
# print("Hii") 
# indentation - 4 empty spaces at the beginning of the line 
# Indentation space will denote whether a line will belong to specific block or not 

# if - else 
# if the condition is true then code present inside if block will get executed and else block will not get executed 
# if the condition is false, then code present inside if block will not get executed and code present inside else block will get executed 
# else block should be used only with if block
# a = 10 
# if 10 < 15:
#     print("Condition True")
# else:
#     print("Condition False")

# program to check whether a num is positive or negative 
# a = int(input("Enter a number : "))
# if a > 0:
#     print("Positive number")
# else:
#     print("Negative number")

# to check whether the number is odd or even 
a = int(input("Enter a number :"))
# After dividing number with 2, if we get remainder as 0 means, then the number is Even number. Otherwise the number is ODD number
# 2,4,6,8 are even
# 1,3,5,7,9 are odd
if a % 2 == 0:
    print("Even number")
else:
    print("Odd Number")