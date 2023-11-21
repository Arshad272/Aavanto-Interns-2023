# Lamda Functions - One line functions 
# They are also called as Anonymous Functions, why because they don't have name 

# syntax
# variable = lambda parms : expression 

def average_of_3_nums(n1, n2, n3):
    s = n1 + n2 + n3 
    a = s / 3 
    print(f"Average of {n1}, {n2} and {n3} is {a}") 

average = lambda n1, n2, n3 : (n1 + n2 + n3) / 3
# print(average(10,20,30)) 

add = lambda a, b : a + b
print(add(10, 20))

a = 10
b = 20
c = 30
# BODMAS
# print( a + b + c / 3 )
# a + b + c / 3
# 10 + 20 + 30 / 3
# 10 + 20 + 10
# 40
# print( (a + b + c) / 3 )
# (a + b + c) / 3
# (10 + 20 + 30) / 3
# 60 / 3
# 20.0 

 