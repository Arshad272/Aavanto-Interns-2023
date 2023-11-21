# Default value to parameters 
def add(a = 100, b = 50):
    return a + b 
x = 10
y = 20
result = add(50, 60)
# print(result)


def average(n1, n2, n3):
    s = n1 + n2 + n3 
    a = s / 3 
    print(f"Average of {n1}, {n2} and {n3} is {a}") 

# average(n2=10, n3=20, n1=30) 


# args 
# if there is * before parameter name means, then we can pass multiple values/arguments while calling a function
def args( *data ):
    print(data) 
# args(10, 20, 30, 40) 

# kwargs - key word arguments 
# we place two stars (**) before parameter name

def kwargs( **data ):
    print(data)  

kwargs(a = 10, b = 20, c = 'hello', d = 'python')
