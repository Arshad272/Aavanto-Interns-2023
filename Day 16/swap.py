
# a = int(input("Enter value for a : "))
# b = int(input("Enter value for b : "))

# Swaping - exchanging the value of two variables 
# incase , if a = 15 and b = 25 means 
# then , after swapping 
# a will be 25 and b will be 15

# print("Before Swapping")
# print(f"The value of a is {a} and b is {b}")
# using temp variable 
# temp = a  # 15
# a = b     # 25   
# b = temp  # 15

# a, b  =  b, a 

# print("After Swapping")
# print(f"The value of a is {a} and b is {b}")


lst = [10,20,30,40,50,60]
print(lst)
temp = lst[0]     # 10
lst[0] = lst[-1]  # 60
lst[-1] = temp    # 10
print("After swapping first and last element")
print(lst) 