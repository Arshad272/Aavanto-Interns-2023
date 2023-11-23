# Recursion
# The function call will be present inside the same function itself

def hello(num):
    if num == 1:
        print(num)
        print("Program ended!")
    else:
        print(num)
        hello(num-1)
# hello(5)

# recursion limit - 1000
def fun():
    print("Hello")
    fun()
fun()