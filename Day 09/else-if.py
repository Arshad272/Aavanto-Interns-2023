# To check more than one condition we can use elif in python

# syntax
# if condition : 
#     code
# elif condition : 
#     code
# elif condition : 
#     code
# elif condition : 
#     code
# elif condition : 
#     code
# else 
#     code

marks = int(input("Enter marks : ")) 
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade D")

